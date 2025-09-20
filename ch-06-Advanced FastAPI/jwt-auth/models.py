# models.py

from pydantic import BaseModel

# Pydantic models for user data
class User(BaseModel):
    username: str
    password: str

# Model for user data stored in the database
class UserInDB(User):
    hashed_password: str