#code for database_handler
import sqlite3

class database_worker:

    #connects to the database
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    #search for an item and return it as an output
    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    #save new data into the database
    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    #cut the connection
    def close(self):
        self.connection.close()

#password encryption
from passlib.hash import sha256_crypt

# Create an object of the class CryptContect
hasher = sha256_crypt.using(rounds=30000)
#recieves the password and returns the hash
def encrypt_password(user_password):
    return hasher.hash(user_password)

def check_password(hashed_password, user_password):
    return hasher.verify(user_password, hashed_password)

hash = encrypt_password("password123")
print(hash)
