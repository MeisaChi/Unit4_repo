# Unit 4 project: Cafe sharing social network

![](https://github.com/MeisaChi/Unit4_repo/blob/main/Screenshots/thumbnail.jpeg)
*“パステルカラーの外観が可愛いカフェ / ワルシャワ / ポーランドの写真素材.” 旅パレット, 4 June 2019, https://decorate-my-trip.com/poland-warsaw-shabby-chic/. Accessed 13 April 2023.*


## Criteria A: Planning

## Problem definition
**Client:** Myself

**Context:** The client, (myself) likes to travel during long term breaks, and especially enjoys going to different cafes in the travelled region. But it is always difficult to find an good cafe, as the client has to look at a lot of components to decide. The client is very picky in food, the appearence of the cafe, and also as a student, the client has to know the price of the food before going to the cafe. This process of finding a cafe usually takes a long time, as the client has to search through different websites to find a favourite, and go on to other websites to find the other menus and the prices. 

**Problem:** The client is finding difficulties to find a cafe that fits their criteria

## Proposed Solution


### Design Statement

## Justification

### Python

### CSS

### html

[^1]:
[^2]: 

## Success criteria
1. Success Criteria
2. Success Criteria
3. Success Criteria
4. Success Criteria
5. Success Criteria
6. Success Criteria

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
This is the python code that actually connects the database into the python file. 

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
This is on another file, secure_password.py. first, it starts with importing sha256_crypt from passlib.hash which is the library that allows the user to use a hashing system. hasher will be the value for the password that is hashed. 

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
