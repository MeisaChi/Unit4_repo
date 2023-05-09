# Unit 4 project: Cafe sharing social network

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Screenshots/thumbnail.jpeg)
*“パステルカラーの外観が可愛いカフェ / ワルシャワ / ポーランドの写真素材.” 旅パレット, 4 June 2019, https://decorate-my-trip.com/poland-warsaw-shabby-chic/. Accessed 13 April 2023.*


## Criteria A: Planning

## Problem definition

**Context:** The client is a high school students, who like so travel, and enjoys going to different cafes. But whenever the client is trying to find a cafe to go to, they always striggle, as the client has to look at the different components such as the concept of the cafe, the location and the price range of the food sold in the cafe. And usually, that includes looking through different websites to find each components of information. As looking through different websites takes time, the client is hoping for a simple platform. This is, where they can create an editable account and login to make the information (name of the cafe, price, location) into a single post, as well as also look at other's reccomendations, saving ones that the client finds interesting. Also, as the client is a traveller, they want to be able to search for a specific component (name of the cafe, price, location) to make the process of finding cafes easier.

**Problem:** The client is a student with limited budget, finding difficulties to find a cafe that fits their criteria

## Proposed Solution

Considering the client's budget limitations and the context of the problem, the solution that I propose for the client is using Python, CSS and html to create a Social Media.

### Design Statement
I will design a social media using Pycharm, which will be a website, by using languages, Python to code the different pages in the website, html to create the components on the pages, and CSS to make the design of the pages nice, and SQLite to keep data inputs by the users. To solve the problem, the website will allow the client to login and create accounts, make a post on a cafe that includes the name, context and location, find an specific account and look at their posts. When an account is created, their username, password (securely stored by hashing) and email will be recorded in a database. 

## Justification

### Python
One of the reason I chose Python is because it is one of the fastest-growing languages in the world, as it is considered as one of the best programming languages for machine learning[^1]. Python runs very fast. As it is very easy to learn and simple, it would be easy for the client to use, without any complex systems, and also with it's simplicity it will be open for any further developers to improve my software. Another key points about Python is that as it is deeply supported by different communities[^1], it has many different accessible libraries, which makes it really flexible, and using the different libraries allowed us to use html and CSS without any issues. The flexibilities of possibilities in Python allows us developers to easily find and add different functions in our app. This solution includes functions in different fields such as an website, different screens, databases, and tables. These different functions are all available in Python, therefore I chose to provide a program using Python as a solution.

### SQLite
The advantage of using SQLite is that it is very simple and easy to use. SQLite is easy to install and use, and it becomes a single file when saved[^2]. It is also accessible in different devices from home devices (phones) to professional devices (airplanes). SQLite does not need administration, and also does not need a server to run. This means it requires minimal support from the operating system or external library[^3]. This makes the website flexible and usable in any device, which is good for a social media, because it is pointed towards varied audiences. And in SQLite, a value can be stored in any value in any column, regardless of the data type[^3]. This becomes very important in our App, because we are creating different attributes that the user can input and they are in different values (strings and integers).

### Flask

[^1]: “Top 10 Reasons Why Python is So Popular With Developers in 2023.” upGrad, 29 September 2022, https://www.upgrad.com/blog/reasons-why-python-popular-with-developers/. Accessed 1 March 2023.
[^2]: “Appropriate Uses For SQLite.” SQLite, 16 December 2022, https://www.sqlite.org/whentouse.html. Accessed 1 March 2023.
[^3]: “What is SQLite? Top SQLite Features You Should Know.” SQLite Tutorial, https://www.sqlitetutorial.net/what-is-sqlite/. Accessed 1 March 2023.


## Success criteria
1. The user can login or create an account and the account data will be securely stored in a database 'social_net.db'
2. The user can edit their account, meaning that the username and the email of the account can be changed
3. The user can make a post, which will include a title (name of the cafe), context, price range and location
4. The user can look at other people's posts
5. The user can bookmark posts and delete bookmarks, which will be saved in their bookmarks folder
6. The user is able to search for a post using a specific word 

# Criteria B: Design

## System Diagram
![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/SystemDiagram.png)
**Fig.1** *System diagram for the Cafe social media.*  
Shows the connection between the input, output and the program. The program gets an input from the user input on keyboard and the trackpad, which is transfered to the computer, then the Mac computer uses Python (includes Pycharm, CSS and HTML) to configurate the inputs. When the program runs, the GUI screen is shown on the computer screeen as an output.

## Wireframe Diagram
![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/wireframe.jpg)
**Fig.2** *Wireframe diagram for the Cafe social media.*  
Shows all the screens and the connections between the different screen, which is basically which button leads to which screen.

## ER Diagram
![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/ER.jpg)
**Fig.3** *ER diagram for the database in the Cafe social media*  
The ER diagram shows the different tables 'users', 'posts' and 'bookmarks', as well as it's different properties within the database 'social_net.db', and it's connection to each other.

## UML Diagram
![]()
**Fig.4** *UML diagram for the OOP classes in the Cafe social media*

## Flow Diagrams
![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/flow_in.jpg)
**Fig.5** *Flow diagram for the Logging in function in the Cafe social media*

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/flow_out.jpg)
**Fig.5** *Flow diagram for the Logging out function in the Cafe social media*

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/flow_post.jpg)
**Fig.5** *Flow diagram for the posting function in the Cafe social media*


## Database Storage 
The data of the different user information and post information will be stored in a SQLite database 'social_net.db'.  
### Users 
| id | uname | email | password |
|-|-|-|-|
| 1 (int. primary key) | Bob. (Str) | bob@xyz.com (Str) | $5$rounds=30000$... (str) |
### Posts 
| id | title | content | price | location | user_id |
|-|-|-|-|-|-|
| 1 (int. primary key) | Cat cafe (str) | A cafe that has many different cats. Very nice (str) | 1000-2000 yen (str) | Tokyo (str) | 1 (int) |
### Bookmarks 
| id | title | content | price | location | user_id | cookie |
|-|-|-|-|-|-|-|
| 7 (int. primary key) | Boardgame Cafe (str) | There is a board game cafe, nice and simple (str) | 2000-3000 yen (str) | Karuizawa (str) | 2 (int) | 2 (int) |



## Test Plan
| Description | Category | Input | Expected Output | Purpose | Success Criteria |
|-|-|-|-|-|-|


## Record of Tasks
| Task No | Planned Action | Planned Outcome | Time estimate | Target completion date | Criterion |
|-|-|-|-|-|-|
| 1 | Find a thumbnail picture | A thumbnail picture that shows up at the top of my github documentation | 5mins | Apr 13 | A |
| 2 | Write my problem definition | A problem definition on my github documentation | 20mins | Apr 13 | A |
| 3 | Wite a justification for python | A justification for python on my github documentation | 5mins | Apr 19 | A |
| 4 | Wite a justification for SQLite | A justification for SQLite on my github documentation | 5mins | Apr 19 | A |
| 5 | Propose a solution | A proposed solution on github documentation | 15mins | Apr 19 | A |
| 6 | Wite a design statement | A design statement on my github documentation | 15mins | Apr 19 | A |
| 7 | Create a success criteria | A finished criteria on my github documentation | 10mins | Apr 19 | A |
| 8 | Wite a justification for CSS | A justification for CSS on my github documentation | 15mins | Apr 19 | A |
| 9 | Wite a justification for HTML | A justification for HTML on my github documentation | 15mins | Apr 19 | A |
| 10 | Import from unit 3 and add explanations for Database worker | A explanation for Database worker on my github documentation | 5mins | Apr 24 | C |
| 11 | Import from unit 3 and add explanations for Hashing the password | A explanation for Hashing the password on my github documentation | 5mins | Apr 24 | C |
| 12 | Create a wireframe diagram | Wireframe diagram on my github documentation | 30mins | Apr 24 | B |
| 13 | Code | Coding progress on my website | 3hrs | Apr 25 | C |
| 14 | Code | Coding progress on my website | 2hrs | Apr 28 | C |
| 15 | Code | Coding progress on my website | 2hrs | May 1 | C |
| 16 | Code | Coding progress on my website | 3hrs | May 5 | C |
| 17 | Work on Criteria C | Finalize, adjust, write descriptions for Criteria C | 2hrs | May 8 | C |

# Criteria C: Development
## Existing tools

## Basic programs
### Imports

```.py
from flask import Flask, render_template, request, redirect, url_for, make_response
from my_lib import database_worker, encrypt_password, check_password
```
This is the items that are imported into the python file. Flask is the import that helps import other libraries that becomes helpful when connecting html to Python, and they make the current and the further development easier. 

My_lib is a library that I have created, which includes the database worker and the functions for hashing and unhashing the password. Usability of these codes are introduced below.


### Database worker
```.py
**#database worker
class database_worker:

    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()**
```
As the users need their information and post information has to be stored in an another database, this is the code which connects the data to the python problem.

Connection and cursor allows us to directly connect to the database, search is used for finding and bringing data from the database, save is for adding and uploading any data into the database, and close is for ending the connection between the python file and the database.

### Hashing the password
```.py
from passlib.hash import sha256_crypt

# Create an object of the class CyptContect
hasher = sha256_crypt.using(rounds=30000)
#recieves the password and returns the hash
def encrypt_password(user_password):
    return hasher.hash(user_password)

def check_password(hashed_password, user_password):
    return hasher.verify(user_password, hashed_password)

hash = encrypt_password("password123")
print(hash)
```
The client also needs the password to be securely stored, for their account to not get stolen. This block of code, allows the program to save in to the database a user's password hashed, and unhash the password when the password has to be matched. 

The code starts with importing sha256_crypt from passlib.hash which is the library that allows the user to use a hashing system. hasher will be the value for the password that is hashed. 

encrypt_password will take an input value 'user_password', and it will return hasher.hash which means that it will return a hashed password.

check_password will take 2 inputs, hashed_password and user_password, and then using verify from the library, it will compared the hashed password and the user password (the user input and the password in the database)

The last code is made for testing the hashing system, because we have to see if it is securely hashed.

### Running the app
```.py
# at the start of the program
app = Flask(__name__)

# at the end of the program
if __name__ == '__main__':
    app.run()
```
This is the code that is used to create and run the app. This is significant for the program, because withought this, there wouldn't be any app.

### Preparing the database
```.py
def create_database():
    db = database_worker("social_net.db")
    query_user = """CREATE table if not exists users (
        id INTEGER PRIMARY KEY,
        uname TEXT,
        email TEXT,
        password TEXT
    )
    """
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
```
Using this create database code, the different tables are created (for users, posts and bookmarks) and saved into the database "social_net.db", which is an SQLite database file. These tables are significant for this program, as all the user inputs will be saved in here. 

### The original page
```.py
@app.route('/')
@app.route('/index')
def index():  # put application's code here
    return redirect('login')
```
App.route will create a webpage, and a name can be set for the route of a page. In the original page that doesn't have any additional routes, and in the index page, it will directly go to the login page.

### Using POST to move variable from html file to Python

```.py
@app.route('/login',methods=['GET','POST'])
```
This code in Python is justifying that there is a post method used within the webpage

```.html
<form method="post" class="container">
    <h2>Login</h2>
        <div>
            <label for="">Email</label>
            <input type="email" name="email">
        </div>
        <div>
            <label for="">Password</label>
            <input type="password" name="passwd">
        </div>
        <div>
            <input type="submit"  class="button" name="" value="Log In">
            <a href="{{ url_for("signup") }}"  class="button">Sign up</a>
        </div>
</form>
```
On the html file, the part where the 'POST' method occurs has to be assigned, and in this example, and in this example there has to be a user input for the 'POST' to happen

```.py
def login():
    msg=""
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['passwd']
```
Back in the Python file, when there is a 'POST' in the html file, it will save the inputs in the forms (email, password) as an individual variable. This is used in anywhere that requires an input, so in the login, signup, editing posts, editing profile and creating a bookmark uses this 'POST' function.

## Matching the user's requirements

### Logging in, logging out - 1/2SC.1 
When it comes to social media, it is necessary that the user can login and logout whenever they want to. And, the database will have different accounts, and it is important for the program to know which users are logged in to the website, and which users are logged out from the website. 

As shown above in the 'The original page' from Basic programs, when the user opens the website, it automatically redirects to the login page. 

```.html
<form method="post" class="container">
    <input type="submit"  class="button" name="" value="Log In">
    <a href="{{ url_for("signup") }}"  class="button">Sign up</a>
</form>
```
This an extracted html code for the login screen, basically requests a method after an input (pressing the Log in button) is made. The one underneath is a link that redirects to the sign up screen when pressed.

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/logsignbutton.png)
**Fig.** *Buttons for login and sign up.*  

```.py
@app.route('/login',methods=['GET','POST'])
def login():
    msg=""
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
                msg = "password does not match"
        else:
            msg = "user does not exist"
    return render_template("login.html", message=msg)

```
After getting a post method and collecting data from the user input on the website, the program will use database_worker introduced above, to find an account that matches the inputs. Then, using check_password, the program compares the input in the password form, the password from the database, with hashed/unhashed matched. 

If the user is able to successfully login, they are redirected to the 'timeline' page, the program gets the user id from the account data collected above, and a cookie is set as the user id. 

Whenever the login doesn't work, it shows an error message with what is wrong with the input. This is done by message being blank at the start, and a string is put into the message when the program recieves a post method, but unable to login.

```.html
{% if message %}
<div class="error"><p>Error: {{ message }}</p></div>
{% endif %}
```
This html code is saying that if there is a message, in other words, if the message isn't blank, it shows "Error:" and the message set above in the python code. 


![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/error1.png)
**Fig.** *Example for when a user inputs a wrong email, the error message will show up like this.*  



```.py
@app.route('/logout',methods=['GET','POST'])
def logout():
    response = make_response(redirect('login'))
    response.set_cookie("user_id","",expires=0)
    return response
```
Shown above is the python code for the user to logout from their account. When the user is directed to the logout page, the page will immediately redirect the user to the login page, and the cookie will be expired. This is how the program differentiates between logged in and logged out users. 

### Registering an account - 2/2SC.1 
```.py
@app.route('/signup',methods=['GET','POST'])
def signup():
    msg = ""
    if request.method == 'POST':
        uname = request.form['uname']
        email = request.form['email']
        passwd = request.form['passwd']
        passwd2 = request.form['passwd2']
        db = database_worker("social_net.db")
        if len(passwd) <6:
            msg = "password has to be longer than 6 letters"
        elif passwd != passwd2:
            msg = "password do not match"
        else:
            query = f"""Insert into users(uname, email, password) values
                    ('{uname}','{email}','{encrypt_password(passwd)}')"""
            db.run_save(query)
            response = make_response(redirect('login'))
            return response
        db.close()
    return render_template("signup.html", message=msg)
```

The system for sign up is pretty similar to login. The dfferences are that:
- The system checks if the input matches the other input (password and password confirmation)
- Error messages: Password has to be longer than 6 letters, password has to match
- After a successful password check, the collected data will all be inserted into the table: users
- When saving data, the password will be secured (hashed) by using 'encrypt_password'.


![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/tab_db.png)
**Fig.** *Table of users in social_net.*  


### Editing the account - SC.2
When creating an account, the user should have the rights to edit and change their email and username.

```.html
<p>Current username is: {{ u[1] }}</p>
<input type="text" name="uname" placeholder="New username">
<p>Current email is: {{ u[2] }}</p>
<input type="text" name="email" placeholder="New email">
```
This html code allows the user to see their current username and email, with the place to input their new account information below.

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/editacc.png)
**Fig.** *Editting data page.*  

```.py
@app.route('/users/editacc', methods=['GET', 'POST'])
def editacc():
    cookie = int(request.cookies.get('user_id'))
    db = database_worker("social_net.db")
    user = db.search(f"Select * from users where id ={cookie}")
    response = render_template("editacc.html", cookie=cookie, user=user)
```
For the program to show the current username and email, as soon as the user is on edit account, the program gets the current logged in user's user id by getting the cookie. Using the user id, the program gets the the whole list of user with the matched user id.

```.py
if request.method == 'POST':
    uname = request.form['uname']
    email = request.form['email']
    print(uname)
    db = database_worker("social_net.db")
    if uname:
        query = f"""update users set uname = '{uname}' where id = {cookie}"""
        db.run_save(query)
    if email:
        query = f"""update users set email = '{email}' where id = {cookie}"""
        db.run_save(query)
    db.close()
    response = redirect('/timeline')
return response
```
When a post method is requested, the program collects the user inputs. The user may desire to change only their username or email, so the program for updating the database to the new collected data only happens if there is an input in either of the attributes. In the end, the user is directed back to the timeline.

### Creating a post - SC.3
The main purpose of this app is for the client to record information of any cafe in a single post.

```.html
<input type="text" name="title" placeholder="Title">
<textarea name="Content"  rows="5" cols="80" placeholder="Content"></textarea>
<input type="text" name="price" placeholder="Price range">
<input type="text" name="location" placeholder="Location">
```
When using the posting function, the content of the post might become slightly longer. Therefore, for the place to input context, instead of an text input, a textarea is used. This way, even when the user types beyond the width of the textbox, it will automatically go to a new line.


![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/makepost.png)
**Fig.** *Actual functionality of the use of textarea in html.*  


### Post definition  - SC.4
### Bookmark function - SC.5
### Searching function - SC.6


## 
```.py
```

## 
```.py
```

## 
```.py
```

## 
```.py
```

## 
```.py
```

### 
```.py
```

## 
```.py
```





## Screen Shots from the app
![]()
**Fig.**
**


# Criteria D: Functionality
## Video
[CLICK HERE FOR THE VIDEO]()
