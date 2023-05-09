# Unit 4 project: Cafe sharing social network

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Screenshots/thumbnail.jpeg)
*“パステルカラーの外観が可愛いカフェ / ワルシャワ / ポーランドの写真素材.” 旅パレット, 4 June 2019, https://decorate-my-trip.com/poland-warsaw-shabby-chic/. Accessed 13 April 2023.*


## Criteria A: Planning

## Problem definition

**Context:** The client, a student studying in a high schools likes to travel during long term breaks, and especially enjoys going to different cafes in the travelled region. But it is always difficult to find an good cafe, as the client has to look at a lot of components to decide. The client is very picky in food, the appearence of the cafe, and also as a student, the client has to know the price of the food before going to the cafe. This process of finding a cafe usually takes a long time, as the client has to search through different websites to find a favourite, and go on to other websites to find the other menus and the prices. Therefore, the client is craving for a SNS platform where they can create an account, login and post informations about different cafes, and also save any posts of cafe that they are interested in. 

**Problem:** The client is a student with limited budget, finding difficulties to find a cafe that fits their criteria

## Proposed Solution

Considering the client's budget limitations and the context of the problem, the solution that I propose for the client is using Python, CSS and html to create a Social Media.

### Design Statement
I will design a social media using Pycharm, which will be a website, by using languages, Python to code the different pages in the website, html to create the components on the pages, and CSS to make the design of the pages nice, and SQLite to keep data inputs by the users. To solve the problem, the website will allow the client to login and create accounts, make a post on a cafe that includes the name, context and location, find an specific account and look at their posts. When an account is created, their username, password (securely stored by hashing) and email will be recorded in a database. 

## Justification

### Python
One of the reason I chose Python is because it is one of the fastest-growing languages in the world, as it is considered as one of the best programming languages for machine learning[^1]. Python runs very fast. As it is very easy to learn and simple, it would be easy for the client to use, without any complex systems, and also with it's simplicity it will be open for any further developers to improve my software. Another key points about Python is that as it is deeply supported by different communities[^1], it has many different accessible libraries, which makes it really flexible. The flexibilities of possibilities in Python allows us developers to easily find and add different functions in our app. This solution includes functions in different fields such as an App, different screens, databases, and tables. These different functions are all available in Python, therefore I chose to provide a program using Python as a solution.

### SQLite
The advantage of using SQLite is that it is very simple and easy to use. SQLite is easy to install and use, and it becomes a single file when saved[^2]. It is also accessible in different devices from home devices (phones) to professional devices (airplanes). SQLite does not need administration, and also does not need a server to run. This means it requires minimal support from the operating system or external library[^3]. As well as KivyMD, this makes SQLite flexible and usable in any device. And in SQLite, a value can be stored in any value in any column, regardless of the data type[^3]. This becomes very important in our App, because we are creating different attributes that the user can input and they are in different values (strings and integers).

### CSS
CSS can be written with simple codes, which means that the number of lines needed for coding the UI design is less. This will allow the program to run faster than when they have more lines of code[^4]. As well as it being light and fast, CSS allows the program to apply a single style sheet on all the assigned pages[^4], which means that all the pages in the website will look united, and this project includes making several pages. Another advantage in using CSS is that it has a user-friendly design, with logical buttons and labels[^4] which enrich the user experience when accessing the website.

### HTML
HTML is an open-source program, which can be implemented free of cost[^5], which matches the client's budgetary restricitions. As well CSS, HTML is simple and light in weight[^5]. HTML can also be flexible to adapt on different platforms[^5], which also helps the client as they are a student which means that they might use their phone or computer. Another advantage is that HTML is easy to be used with other programming languages[^5], which in this case, as it uses other language such as Python and CSS, using HTML will allow the program to be simple and open for development.


[^1]: “Top 10 Reasons Why Python is So Popular With Developers in 2023.” upGrad, 29 September 2022, https://www.upgrad.com/blog/reasons-why-python-popular-with-developers/. Accessed 1 March 2023.
[^2]: “Appropriate Uses For SQLite.” SQLite, 16 December 2022, https://www.sqlite.org/whentouse.html. Accessed 1 March 2023.
[^3]: “What is SQLite? Top SQLite Features You Should Know.” SQLite Tutorial, https://www.sqlitetutorial.net/what-is-sqlite/. Accessed 1 March 2023.
[^4]: “What Is CSS and Why Should You Use It?” Devmountain, https://devmountain.com/blog/what-is-css-and-why-use-it/. Accessed 19 April 2023.
[^5]: Goyal, Yashi. “Advantages of HTML | Top 10 Amazing Advantages of HTML.” eduCBA, https://www.educba.com/advantages-of-html/. Accessed 19 April 2023.


## Success criteria
1. The user can login or create an account and the account data will be securely stored
2. The user can switch between different pages
3. The user can make a post, which will include a title (name of the cafe), context, price range and location
4. The user can look at other people's posts
5. The user can bookmark posts, which will be saved in their bookmarks folder
6. The user is able edit their profile, which means that they can change their email or username

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

## Python Code

## Imports

```.py
from flask import Flask, render_template, request, redirect, url_for, make_response
from my_lib import database_worker, encrypt_password, check_password
```
This is the items that are imported into the python file. Flask is the import that helps import other libraries that becomes helpful when connecting html to Python, and they make the current and the further development easier. 

My_lib is a library that I have created, which includes the database worker and the functions for hashing and unhashing the password. Usability of these codes are introduced below.


## Database worker
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

## Hashing the password
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

## Running the app
```.py
# at the start of the program
app = Flask(__name__)

# at the end of the program
if __name__ == '__main__':
    app.run()
```
This is the code that is used to create and run the app. This is significant for the program, because withought this, there wouldn't be any app.

## Preparing the database
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

## The original page
```.py
@app.route('/')
@app.route('/index')
def index():  # put application's code here
    return redirect('login')
```
App.route will create a webpage, and a name can be set for the route of a page. In the original page that doesn't have any additional routes, and in the index page, it will directly go to the login page.

## Using POST to move variable from html file to Python

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
