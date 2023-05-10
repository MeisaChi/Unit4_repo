#imports
from flask import Flask, render_template, request, redirect, url_for, make_response
from my_lib import database_worker, encrypt_password, check_password

#connect to flask
app = Flask(__name__)

#create a table
def create_database():
#users
    db = database_worker("social_net.db")
    query_user = """CREATE table if not exists users (
        id INTEGER PRIMARY KEY,
        uname TEXT,
        email TEXT,
        password TEXT
    )
    """
#posts
    query_post = """CREATE table if not exists posts (
        id INTEGER PRIMARY KEY,
        title VARCHAR(100),
        content TEXT,
        price TEXT,
        location TEXT,
        user_id INTEGER, 
        FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
    )
    """

    db.run_save(query_user)
    db.run_save(query_post)
    db.close()

#add users
def populate_db():
    users = [("Bob","bob@xyz.com", "qwerty"), ("Kevin","kevin@nbc.com","password123")]
    db = database_worker("social_net.db")
    for u in users:
        uname, email, pwd = u
        query = f"""Insert into users(uname, email, password) values
        ('{uname}','{email}','{encrypt_password(pwd)}')"""
        db.run_save(query)
    db.close()

#login page
@app.route('/login',methods=['GET','POST'])
def login():
    # error message
    msg=""
    # when the login button is pressed
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['passwd']
        db = database_worker("social_net.db")
        user = db.search(f"SELECT * from users where email = '{email}'")
        if user:
            user = user[0] #search function returns a list
            id, uname, email_db, hashed = user
            if check_password(hashed_password=hashed, user_password=passwd):
                response = make_response(redirect('timeline'))
                response.set_cookie('user_id', f"{id}") #cookie is a string
                return response
            else:
                # error message1
                msg = "password does not match"
        else:
            # error message 2
            msg = "user does not exist"
    return render_template("login.html", message=msg)

@app.route('/signup',methods=['GET','POST'])
def signup():
    # error message
    msg = ""
    # when the user presses the sign up button to create a new account
    if request.method == 'POST':
        uname = request.form['uname']
        email = request.form['email']
        passwd = request.form['passwd']
        passwd2 = request.form['passwd2']
        db = database_worker("social_net.db")
        if len(passwd) <6:
            # error message 1
            msg = "password has to be longer than 6 letters"
        elif passwd != passwd2:
            # error message 2
            msg = "password do not match"
        else:
            query = f"""Insert into users(uname, email, password) values
                    ('{uname}','{email}','{encrypt_password(passwd)}')"""
            db.run_save(query)
            response = make_response(redirect('login'))
            return response
        db.close()
    return render_template("signup.html", message=msg)

# logout function
@app.route('/logout',methods=['GET','POST'])
def logout():
    # goes back to the login page
    response = make_response(redirect('login'))
    # removes cookie
    response.set_cookie("user_id","",expires=0)
    return response

# profile page for each user
@app.route('/users/<user_id>', methods=['GET', 'POST'])
def profile(user_id:int):
    # if there is no user logged in, it will immediately go to the login page
    if request.cookies.get('user_id'):
        # when the user presses 'edit post'
        if request.method == 'POST':
            postname = request.form.get("post_name")
            print(f"request.method is {request.method}")
            print(f"the name is {postname}")
            return redirect(f'/editpost?postname={postname}')
        # For the 'edit post' to only show on the logged in user's posts
        AccCheck = False
        db = database_worker("social_net.db")
        user, posts = None, None
        user = db.search(f"Select * from users where id ={user_id}")
        if user:
            posts = db.search(f"Select * from posts where user_id = {user_id}")
            user = user[0]
            cookie = request.cookies.get('user_id')
            # if the user id of the posts are the same as the cookie
            if int(user_id) == int(cookie):
                AccCheck = True
        return render_template("profile.html", user=user, posts=posts, AccCheck=AccCheck)
    else:
        return redirect('login')

# editing the account page
@app.route('/users/editacc', methods=['GET', 'POST'])
def editacc():
    # if there is no user logged in, it will immediately go to the login page
    if request.cookies.get('user_id'):
        cookie = int(request.cookies.get('user_id'))
        db = database_worker("social_net.db")
        # gets the data of user currently logged in
        user = db.search(f"Select * from users where id ={cookie}")
        response = render_template("editacc.html", cookie=cookie, user=user)
        # when the user presses 'change' button
        if request.method == 'POST':
            uname = request.form['uname']
            email = request.form['email']
            print(uname)
            db = database_worker("social_net.db")
            # if there is an input, it will change the value on the database
            if uname:
                query = f"""update users set uname = '{uname}' where id = {cookie}"""
                db.run_save(query)
            if email:
                query = f"""update users set email = '{email}' where id = {cookie}"""
                db.run_save(query)
            db.close()
            response = redirect('/timeline')
        return response
    else:
        return redirect('login')

# will directly go to the login page
@app.route('/')
@app.route('/index')
def index():  # put application's code here
    return redirect('login')

# the timeline or the home screen
@app.route('/timeline', methods=['GET', 'POST'])
def timeline():
    # if there is no user logged in, it will immediately go to the login page
    if request.cookies.get('user_id'):
        if request.method == 'POST':
            # if the request was a search
            if 'search' in request.form:
                search_query = request.form.get('search')
                db = database_worker("social_net.db")
                posts = db.search(f"SELECT * FROM posts WHERE title LIKE '%{search_query}%' OR content LIKE '%{search_query}%' OR location LIKE '%{search_query}%'")
                uname = ['test']
                cookie = int(request.cookies.get('user_id'))
                for p in posts:
                    userid = p[5]
                    unamelist = db.search(f"SELECT uname FROM users WHERE id={userid}")
                    uname.append(unamelist[0][0])
                return render_template("timeline.html", posts=posts, uname=uname, cookie=cookie)

            # if the request is an edit post
            elif 'edit' in request.form:
                postname = request.form.get("post_name")
                print(f"request.method is {request.method}")
                print(f"the name is {postname}")
                return redirect(f'/editpost?postname={postname}')

            # if the request was a bookmark
            elif 'bookmark' in request.form:
                postname = request.form.get("post_name")
                # get the cookie so it can be added to the bookmarks table as a new attribute from posts
                cookie = int(request.cookies.get('user_id'))
                print(postname)
                db = database_worker("social_net.db")
                title = db.search(f"SELECT title FROM posts WHERE title == '{postname}'")
                content = db.search(f"SELECT content FROM posts WHERE title == '{postname}'")
                price = db.search(f"SELECT price FROM posts WHERE title == '{postname}'")
                location = db.search(f"SELECT location FROM posts WHERE title == '{postname}'")
                user_id = db.search(f"SELECT user_id FROM posts WHERE title == '{postname}'")
                print(title, content, price, location, user_id, cookie)
                query = f"""Insert into bookmarks(title, content, price, location, user_id, cookie) values
                                    ('{title[0][0]}','{content[0][0]}','{price[0][0]}','{location[0][0]}','{user_id[0][0]}','{cookie}')"""
                db.run_save(query)
                db.close()
                # goes to the bookmark page so that the user doesn't save a post twice
                return redirect('bookmarks')

        uname = ['test']
        if request.cookies.get('user_id'):
            db = database_worker("social_net.db")
            # gets all of the posts
            posts = db.search("SELECT * From posts")
            for p in posts:
                cookie = int(request.cookies.get('user_id'))
                print(p[5])
                userid = p[5]
                unamelist = db.search(f"SELECT uname From users where id={userid}")
                uname.append(unamelist[0][0])
                print(uname)
            print(posts)
            return render_template("timeline.html", posts=posts, uname=uname, cookie=cookie)
        else:
            return redirect('login')
    else:
        return redirect('login')

# bookmarks page
@app.route('/bookmarks', methods=['GET', 'POST'])
def bookmarks():
    # if there is no user logged in, it will immediately go to the login page
    if request.cookies.get('user_id'):
        cookie = int(request.cookies.get('user_id'))
        db = database_worker("social_net.db")
        # gets posts that are bookmarked by the currently logged in user
        posts = db.search(f"SELECT * From bookmarks where cookie={cookie}")
        response = render_template("bookmarks.html", posts=posts)
        # when the user presses the delete button
        if request.method == 'POST':
            postname = request.form.get("post_name")
            print(postname)
            db = database_worker("social_net.db")
            query = f"""DELETE from bookmarks where id ={postname}"""
            db.run_save(query)
            db.close()
            response = redirect("bookmarks")
        return response
    else:
        return redirect('login')

# editing posts page
@app.route('/editpost', methods=['GET', 'POST'])
def editpost():
    # if there is no user logged in, it will immediately go to the login page
    if request.cookies.get('user_id'):
        postname = request.args.get('postname')
        print(f"editing {postname}")
        db = database_worker("social_net.db")
        post = db.search(f"Select * from posts where title ='{postname}'")
        print(post)
        response = render_template("editpost.html", post=post)
        if request.method == 'POST':
            # when change button is pressed
            if 'edit' in request.form:
                title = request.form['Title']
                content = request.form['Content']
                price = request.form['Price']
                location = request.form['Location']
                db = database_worker("social_net.db")
                if title:
                    query = f"""update posts set title = '{title}' where title = '{postname}'"""
                    db.run_save(query)
                if content:
                    query = f"""update posts set content = '{content}' where title = '{postname}'"""
                    db.run_save(query)
                if price:
                    query = f"""update posts set price = '{price}' where title = '{postname}'"""
                    db.run_save(query)
                if location:
                    query = f"""update posts set location = '{location}' where title = '{postname}'"""
                    db.run_save(query)
                db.close()
                response = redirect('/timeline')
            else:
                # when delete button is pressed
                db = database_worker("social_net.db")
                query = f"""DELETE from posts where title ='{postname}'"""
                db.run_save(query)
                db.close()
                response = redirect('/timeline')
        return response
    else:
        return redirect('login')

#creating a post page
@app.route('/post', methods=["GET", "POST"])
def post():
    db = database_worker("social_net.db")
    # if there is no user logged in, it will immediately go to the login page
    if request.cookies.get('user_id'):
        if request.method == 'POST':
            user_id=request.cookies.get('user_id')
            title = request.form['title']
            content = request.form['Content']
            price = request.form['price']
            location = request.form['location']
            # checks if there is a title and a content
            if len(title) > 0 and len(content) > 0:
                new_post = f"INSERT into posts (title, content, price, location, user_id) values('{title}','{content}','{price}','{location}',{user_id})"
                db.run_save(query=new_post)
                return redirect('timeline')
        return render_template("post.html")
    else:
        return redirect('login')

# run the website!
if __name__ == '__main__':
    app.run()
