# main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import create_access_token, verify_token
from models import UserInDB
from utils import get_user, verify_password

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token') # Used for creating token

# Endpoint to get current user based on token
@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = get_user(form_data.username) # Fetch user from DB

    if not user_dict: # Check if user exists
        raise HTTPException(status_code=400, detail='Incorrect username') 
    
    if not verify_password(form_data.password, user_dict['hashed_password']): # Verify password
        raise HTTPException(status_code=400, detail='Incorrect password')
    
    access_token = create_access_token(data={'sub': form_data.username}) # Create JWT token
    return {
        'access_token': access_token,
        'token_type': 'bearer'
    } # Return token response


@app.get('/users')
def read_users(token: str = Depends(oauth2_scheme)):
    username = verify_token(token) # Verify token and extract username
    return {'username': username} # Return the username
