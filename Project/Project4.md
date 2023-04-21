# Unit 4 project: Cafe sharing social network

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Screenshots/thumbnail.jpeg)
*“パステルカラーの外観が可愛いカフェ / ワルシャワ / ポーランドの写真素材.” 旅パレット, 4 June 2019, https://decorate-my-trip.com/poland-warsaw-shabby-chic/. Accessed 13 April 2023.*


## Criteria A: Planning

## Problem definition

**Context:** The client, a student studying in a high schools likes to travel during long term breaks, and especially enjoys going to different cafes in the travelled region. But it is always difficult to find an good cafe, as the client has to look at a lot of components to decide. The client is very picky in food, the appearence of the cafe, and also as a student, the client has to know the price of the food before going to the cafe. This process of finding a cafe usually takes a long time, as the client has to search through different websites to find a favourite, and go on to other websites to find the other menus and the prices. 

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
3. The user can make a post, which will include a title (name of the cafe), context and location
4. The user can look at other people's posts
5. The user can bookmark posts, which will be saved in their bookmarks folder
6. The user can log out from the website, which will restrict the accessibility to the website

# Criteria B: Design

## System Diagram
![]()
**Fig.1** *Explanation of figure*  
Explanation

## Database Storage 
The data of the different user information and item information will be stored in a SQLite database ''.  

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

# Criteria C: Development
## Existing tools

## Python Code

### Imports

```.py
```
This is the items that are imported into the python file.


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

## Screen Shots from the app
![]()
**Fig.**
**


# Criteria D: Functionality
## Video
[CLICK HERE FOR THE VIDEO]()
