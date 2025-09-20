# utils.py

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto') # bcrypt is a strong hashing algorithm

# A fake in-memory user "database"
fake_user_db = {
    'johndoe': {
        'username': 'johndoe',
        'hashed_password': pwd_context.hash('secret123')
    }
}

# Function to get a user from the fake database
def get_user(username: str):
    user = fake_user_db.get(username)
    return user

# Function to verify a plain password against a hashed password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)