# Unit 4 project: Cafe sharing social network

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Screenshots/thumbnail.jpeg)
**Fig.1** *“パステルカラーの外観が可愛いカフェ / ワルシャワ / ポーランドの写真素材.” 旅パレット, 4 June 2019, https://decorate-my-trip.com/poland-warsaw-shabby-chic/. Accessed 13 April 2023.*


## Criteria A: Planning

## Problem definition

**Context:** The client is a high school students, who like so travel, and enjoys going to different cafes. But whenever the client is trying to find a cafe to go to, they always struggle, as the client has to look at the different components such as the concept of the cafe, the location and the price range of the food sold in the cafe. And usually, that includes looking through different websites to find each components of information. As looking through different websites takes time, the client is hoping for a simple platform. This is, where they can create an editable account and login to make the information (name of the cafe, price, location) into a single post, as well as also look at other's recommendations, saving ones that the client finds interesting. Also, as the client is a traveller, they want to be able to search for a specific component (name of the cafe, price, location) to make the process of finding cafes easier.

**Problem:** The client is a student with limited budget, finding difficulties to find a cafe that fits their criteria

**Note from the client interview:**

Client 
- [ ] Student—> limited budget 
- [ ] Travel, cafe
- [ ] Research takes time—> Single post
- [ ] Simple, easy
- [ ] Name of the cafe, price, location
- [ ] Other people, share
- [ ] Save functions
- [ ] Search for specific location and others?

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
**Fig.2** *System diagram for the Cafe social media.*  
Shows the connection between the input, output and the program. The program gets an input from the user input on keyboard and the trackpad, which is transfered to the computer, then the Mac computer uses Python (includes Pycharm, CSS and HTML) to configurate the inputs. When the program runs, the GUI screen is shown on the computer screeen as an output.

## Wireframe Diagram
![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/wireframe.jpg)
**Fig.3** *Wireframe diagram for the Cafe social media.*  
Shows all the screens and the connections between the different screen, which is basically which button leads to which screen.

## ER Diagram
![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/ER.jpg)
**Fig.4** *ER diagram for the database in the Cafe social media*  
The ER diagram shows the different tables 'users', 'posts' and 'bookmarks', as well as it's different properties within the database 'social_net.db', and it's connection to each other.

## UML Diagram
![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/uml.jpg)
**Fig.5** *UML diagram for the OOP classes used in the Cafe social media*

## Flow Diagrams
![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/flow_in.jpg)
**Fig.6** *Flow diagram for the Logging in function in the Cafe social media*

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/flow_out.jpg)
**Fig.7** *Flow diagram for the Logging out function in the Cafe social media*

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/flow_post.jpg)
**Fig.8** *Flow diagram for the posting function in the Cafe social media*


## Database Storage 
The data of the different user information and post information will be stored in a SQLite database 'social_net.db'.  
### Users 
| id | uname | email | password |
|-|-|-|-|
| 1 (int. primary key) | Bob. (Str) | bob@xyz.com (Str) | 5$rounds=30000... (str) |
### Posts 
| id | title | content | price | location | user_id |
|-|-|-|-|-|-|
| 1 (int. primary key) | Cat cafe (str) | A cafe that has many different cats. Very nice (str) | 1000-2000 yen (str) | Tokyo (str) | 1 (int) |
### Bookmarks 
| id | title | content | price | location | user_id | cookie |
|-|-|-|-|-|-|-|
| 7 (int. primary key) | Boardgame Cafe (str) | There is a board game cafe, nice and simple (str) | 2000-3000 yen (str) | Karuizawa (str) | 2 (int) | 2 (int) |



1. The user can login or create an account and the account data will be securely stored in a database 'social_net.db'
2. The user can edit their account, meaning that the username and the email of the account can be changed
3. The user can make a post, which will include a title (name of the cafe), context, price range and location
4. The user can look at other people's posts
5. The user can bookmark posts and delete bookmarks, which will be saved in their bookmarks folder
6. The user is able to search for a post using a specific word 


## Test Plan
| Description | Category | Input | Expected Output | Purpose | Success Criteria |
|-|-|-|-|-|-|
| Login: Success | Unit testing | email, password | Go to timeline page, set a cookie | The user has to be able to successfully login when their inputs are matched to the data in the 'users' table | 1 |
| Login: Fail: No user | Unit testing | password | Error message: user does not exist | When there is no user that matches the user input, or there is no input in the email, the login should fail and show an error message | 1 |
| Login: Fail: password | Unit testing | email, wrong password | Error message: password does not match | When the the password does not match the password on the 'users' table, the login should fail and show an error message | 1 |
| Sign up: Success | Unit testing | username, email, password, password confirmation | Go to login page, inputs saved onto database | The user has to be able to successfully create an account when their inputs meet the requirements | 1 |
| Sign up: Fail: password length | Unit testing | username, email, password <6 letters, password confirmation | Error message: password has to be longer than 6 letters | When the the password does not have more than 6 letters, the sign up should fail and show an error message | 1 |
| Sign up: Fail: password confirmation | Unit testing | username, email, password, password confirmation | Error message: password do not match | When the passwords inputted by the user does not match, the sign up should fail and show an error message | 1 |
| Logout | Unit testing | username, email, password, password confirmation | Error message: password do not match | When the passwords inputted by the user does not match, the sign up should fail and show an error message | 1 |
| Edit account | Unit testing | email and / or username | New username / email on the database | The user is able to change their username and / or their email when they want to | 2 |
| Make a post: Success | Unit testing | title, content, price range, location | Post saved onto the posts table | For the user to be able to make any posts and will be shown on the timeline | 3 |
| Make a post: Fail | Unit testing | price range, location | Post not saved onto the posts table | without the title and the content, there will be no posts submitted | 3 |
| Timeline | Unit testing | N/A | All post will be shown in the timeline | The user can look at theirs and other's posts | 4 |
| Save on bookmarks | Unit testing | Press on garbage button | A posts data saved onto the bookmarks table, with the cookie | A logged in user can save any posts into their bookmarks | 5 |
| Search | Unit testing | ANY INPUT | Timeline posts shows posts with the inputted word | The user is able to search for a specific attribute such as location or price | 6 |
| Login, sign up, timeline, bookmarks, profile and edit post | Integration testing | username, email, password, password confirmation, cafe name, location, price range | The user is able to sign up, then login, which will redirect them in the timeline, and from there the user can go to bookmarks, profile, edit post or logout | The user should be able to go to different pages without any difficulties, and create posts | 1, 3, 4, 5 |
| Profile and edit account | Integration testing | email, username | The user is able to access the profile page, and also access edit profile through their own profile page | The user should be able to look at their profiles and change their profiles whenever they want to | 2 |




## Record of Tasks
| Task No | Planned Action | Planned Outcome | Time estimate | Target completion date | Criterion |
|-|-|-|-|-|-|
| 1 | Planning: Meet the client | Identify the client's problem and their requirements | 15mins | Apr 9 | A |
| 2 | Planning: thumbnail | Find a thumbnail picture that comes on the top of my documentation | 5mins | Apr 11 | A |
| 3 | Planning: Problem definition | Write a detailed definition of the client's problem | 15mins | Apr 13 | A |
| 4 | Planning: Design statement | A detailed statement for the program that I am designing | 15mins | Apr 13 | A |
| 5 | Planning: Solution Proposal | A detailed description of the solution that I came up with to fit the needs of the client | 20mins | Apr 15 | A |
| 6 | Planning: Python Justification | A justification for the reason I chose python for this program | 10mins | Apr 19 | A |
| 7 | Planning: SQLite Justification | A justification for the reason I chose SQLite for this program | 10mins | Apr 19 | A |
| 8 | Planning: Flask Justification | A justification for the reason I chose Flask for this program | 15mins | Apr 19 | A |
| 9 | Planning: Success criteria | 6 success criteria that focuses on the client's needs | 20mins | Apr 20 | A |
| 10 | Planning: Check-up | Check with the client whether the proposal and success criteria meets their requirements | 15mins | Apr 24 | A |
| 11 | Design: System diagram | Create a system diagram that shows the connection between inputs and outputs, the program | 30mins | Apr 27 | B |
| 12 | Design: Wireframe diagram | Create a wireframe diagram that shows the different screens available in the website and their connections | 45mins | Apr 27 | B |
| 13 | Design: ER diagram | Create a ER diagram that shows the different databases used in the program | 15mins | Apr 27 | B |
| 14 | Design: UML diagram | Create a UML diagram that shows the OOP classes used in the program | 5mins | Apr 28 | B |
| 15 | Design: Database storage | Shows how the data will be stored in different tables, in social_net.db | 5mins | Apr 29 | B |
| 16 | Design: test plan | A test plan for different functionalities in the program | 30mins | Apr 30 | B |
| 17 | Development: Database worker | Imported and updated from project unit 3, allows the program to connect to the database | 5mins | May 1 | C |
| 18 | Development: Password hasher | Imported and updated from project unit 3, allows password to be hashed and unhashed | 5mins | May 1 | C |
| 19 | Development: Login screen | The user is able to login with a correct combination of email and password, or choose to create an account | 45mins | May 2 | C |
| 20 | Development: Sign up screen | The user is able to input a username, email and password to create an account that will be saved into the database, can be used for logging in | 30mins | May 3 | C |
| 21 | Development: timeline screen | The user can look and bookmark other people's posts or go to their profile, the user can choose to go to bookmarks, post or logout | 60mins | May 5 | C |
| 22 | Development: posting screen | The user enter attributes and create a post where it will be on timeline. They can also edit or delete any posts made by them | 60mins | May 5 | C |
| 23 | Development: profile screen | The user can look at their own profile and choose to edit their own profile, or can look at other user's screen where it will show their posts | 45mins | May 6 | C |
| 24 | Development: Editting an account | The user may input a new username or an email, will be overwritten on talbe 'users' | 30mins | May 7 | C |
| 25 | Development: Editting a post | The user may input any new attributes, will be overwritten on talbe 'posts' | 30mins | May 7 | C |
| 26 | Development: Bookmark screen | The user may look at the bookmarks they have made | 30mins | May 8 | C |
| 27 | Development: logout | The user may logout from an logged in account, will be redirected back to the login screen | 30mins | May 8 | C |
| 28 | Development: Search | The user may input a specific attribute, timeline will only show posts with the attribute | 60mins | May 9 | C |
| 29 | Development: Documentation | Documentation will be made for the programs used to clear the success criteria | 60mins | May 9 | C |
| 28 | Development: Search | The user may input a specific attribute, timeline will only show posts with the attribute | 60mins | May 10 | C |
| 29 | Design: Flow diagram | Flow diagram to show the system behind the Login | 20mins | May 10 | B |
| 30 | Design: Flow diagram | Flow diagram to show the system behind the Logout | 15mins | May 10 | B |
| 31 | Design: Flow diagram | Flow diagram to show the system behind the Posting | 45mins | May 10 | B |
| 32 | Test: Test plan | Run the assigned tests in the test plan | 30mins | May 10 | C |
| 33 | Design: Screenshots | Take screenshots to put on Criterion C | 10mins | May 10 | C |
| 34 | Development: existing tools | Update my existing tools in Criterion C | 5mins | May 9 | C |
| 35 | Planning: Script | Create s script for the criterion D video | 30mins | May 10 | D |


# Criteria C: Development
## Existing tools
Python
CSS
HTML
Flask

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

```.py
@app.route('/post', methods=["GET", "POST"])
def post():
    db = database_worker("social_net.db")
    if request.cookies.get('user_id'):#if there is a user logged in
    if request.method == 'POST':
        user_id=request.cookies.get('user_id')
        title = request.form['title']
        content = request.form['Content']
        price = request.form['price']
        location = request.form['location']
        if len(title) > 0 and len(content) > 0:
            new_post = f"INSERT into posts (title, content, price, location, user_id) values('{title}','{content}','{price}','{location}',{user_id})"
            db.run_save(query=new_post)
            return redirect('timeline')
    return render_template("post.html")
```
This is the code for saving the post to the posts table on the social_net database. Similar to the login, sign up and others, this also collects data from the user input. In here, the user has to have a title and a content(has to be longer than a letter). After a post is made, the user is redirected back to the timeline.


### Show posts and user definition  - SC.4
The client desires to be able to check their own posts as well as other people's posts on cafe, too.
```.py
db = database_worker("social_net.db")
posts = db.search("SELECT * From posts")
for p in posts:
    cookie = int(request.cookies.get('user_id'))
return render_template("timeline.html", posts=posts, uname=uname, cookie=cookie)    
```
In this extracted python code, after the timeline page is loaded, the program gets list of all the post from the posts table in the database. Then, the program will get the cookie (to get the current user logged in).

```.html
{% for p in posts %}
    <div>
    <tbody>
        <h2 class="posttitle">{{ p[1] }}</h2>
        <p><a href="{{ url_for("profile", user_id=p[5]) }}" class="clicktouser">{{ uname[p[0]] }}</a></p>
        <p class="context">{{ p[2] }}</p>
        <p class="price">{{ p[3] }}</p>
        <p class="location">{{ p[4] }}</p>
    </tbody>
    <div class="button-container">
    <form method="post">
    <button class="bookmark" name="bookmark"><ion-icon name="bookmark-outline"></ion-icon></button>
    <input type="hidden" name="post_name" value="{{ p[1] }}">
    {% if cookie==p[5]  %}
    <input type="submit" class="button" name="edit" value="Edit post">
    {% endif  %}
    </form>
```
Here in the timeline html file, for every post, the different attributes for a post are shown. Also, a button with bookmark is shown, and if the cookie (the logged in user) is the same as the user id of a post, it shows an edit post button.

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/timeline.png)

**Fig.** *Posts with and without the edit post button.* 

### Bookmark function - SC.5
Another one of the client's needs was to be able to save posts in bookmarks, delete posts from bookmarks.

```.html
{% if posts %}
{% for p in posts %}
    <div>
    <tbody>
        <h2 class="posttitle">{{ p[1] }}</h2>
        <p class="context">{{ p[2] }}</p>
        <p class="price">{{ p[3] }}</p>
        <p class="location">{{ p[4] }}</p>
    </tbody>
    <div class="button-container">
    <form method="post">
    <button class="bookmark" name="trash"><ion-icon name="trash-outline"></ion-icon></button>
    <input type="hidden" name="post_name" value="{{ p[0] }}">
    </form>
    </div>
    </div>
    <hr>
{% endfor %}
{% else %}
<h2>You do not have any bookmarks</h2>
{% endif %}
```
This is the html for bookmarks page. If there is a post, it shows the post with a trash button on the bottom, and if there are no posts in the bookmark, it will say 'you do not have any bookmarks.'

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/bookmark.png)

**Fig.** *A bookmark page with a bookmark.* 


![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/no_bookmark.png)

**Fig.** *A bookmark page without a bookmark.* 

```.py
elif 'bookmark' in request.form:
    postname = request.form.get("post_name")
    cookie = int(request.cookies.get('user_id'))
    db = database_worker("social_net.db")
    title = db.search(f"SELECT title FROM posts WHERE title == '{postname}'")
    content = db.search(f"SELECT content FROM posts WHERE title == '{postname}'")
    price = db.search(f"SELECT price FROM posts WHERE title == '{postname}'")
    location = db.search(f"SELECT location FROM posts WHERE title == '{postname}'")
    user_id = db.search(f"SELECT user_id FROM posts WHERE title == '{postname}'")
    query = f"""Insert into bookmarks(title, content, price, location, user_id, cookie) values
                        ('{title[0][0]}','{content[0][0]}','{price[0][0]}','{location[0][0]}','{user_id[0][0]}','{cookie}')"""
    db.run_save(query)
    db.close()
    return redirect('bookmarks')
```
This is the python code back in the timeline page. When the bookmark button is pressed, the program collects the name of the post, and also collects the cookie. Then, the every attribute is taken from the table posts in the database where the name of the post matches, and are inserted into a new database called titles. After closing the database, the user is redirected to the bookmarks page.

```.py
@app.route('/bookmarks', methods=['GET', 'POST'])
def bookmarks():
    cookie = int(request.cookies.get('user_id'))
    db = database_worker("social_net.db")
    posts = db.search(f"SELECT * From bookmarks where cookie={cookie}")
    response = render_template("bookmarks.html", posts=posts)
    return response
```
This is the python code running the bookmarks page. First, the program gets the current cookie, and searches the bookmarks table in social_net.db where the collected cookie matches the cookie in the database. The matched posts are saved, and the bookmarks html is rendered.

```.py
if request.method == 'POST':
    postname = request.form.get("post_name") 
    db = database_worker("social_net.db")
    query = f"""DELETE from bookmarks where id ={postname}"""
    db.run_save(query)
    db.close()
    response = redirect("bookmarks")
return response
```
This is the code for deleting posts in bookmarks. A request is sent when the trash button is pressed. The program gets the name of the posts, and from the table bookmarks, deletes the data that matches the collected postname. The user is redirected back to bookmarks.

### Searching function - SC.6
The last requirement was for the client to be able to search for a specific word.

```.py
if 'search' in request.form:
    search_query = request.form.get('search')
    db = database_worker("social_net.db")
    posts = db.search(f"SELECT * FROM posts WHERE title LIKE '%{search_query}%' OR content LIKE '%{search_query}%' OR location LIKE '%{search_query}%'")
    return render_template("timeline.html", posts=posts, uname=uname, cookie=cookie)
```
The search function is made within the timeline, and so when a search request is sent, the word that the user is searching for is collected from the site. Then the program looks at the database to see if there are any posts including that specific word. The timeline page is rendered again, with the renewed list of posts.

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Project/pics/search.png)

**Fig.** *Search bar.* 





## Screen Shots from the app
![]()
**Fig.**
**


# Criteria D: Functionality
## Video
[CLICK HERE FOR THE VIDEO]()
