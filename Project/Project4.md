# Unit 4: 

![]()
*Citation of picture


## Criteria A: Planning

## Problem definition
**Client:** 

**Context:** 

**Problem:** 

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
![](https://github.com/MeisaChi/Unit3_repo/blob/main/Project/Pics/SS_Log.png)
**Fig.11**
*Login Screen*

![](https://github.com/MeisaChi/Unit3_repo/blob/main/Project/Pics/SS_Reg.png)
**Fig.12**
*Signup Screen*

![](https://github.com/MeisaChi/Unit3_repo/blob/main/Project/Pics/SS_Home.png)
**Fig.13**
*Home Screen*

![](https://github.com/MeisaChi/Unit3_repo/blob/main/Project/Pics/SS_pop.png)
**Fig.14**
*Pop up for when the user is logging out*

![](https://github.com/MeisaChi/Unit3_repo/blob/main/Project/Pics/SS_Add.png)
**Fig.15**
*Adding items Screen*

![](https://github.com/MeisaChi/Unit3_repo/blob/main/Project/Pics/SS_Tab.png)
**Fig.16**
*Table Screen*

# Criteria D: Functionality
## Video
[CLICK HERE FOR THE VIDEO]()
