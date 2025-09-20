from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
 
oauth2_scheme =OAuth2PasswordBearer(tokenUrl='token') # URL to get the token


# Endpoint to simulate user login and return a token
@app.post('/token')
def login(username: str = Form(...), password: str = Form(...)): # (...) = required
    if username == 'john' and password == 'pass123':
        return {'access_token': 'valid_token',
                'token_type': 'bearer'}
    raise HTTPException(status_code=400, detail='Invalid username or password')


# Explanation: In a real-world application, you would verify the token's signature, expiration, and other claims.
def decode_token(token: str): # mock function to decode token
    if token == 'valid_token':
        return {'name': 'john'}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid Authentication credentials'
    ) 

# Dependency function to get the current user based on the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)

# Protected route that requires authentication
@app.get('/profile')
def get_profile(user=Depends(get_current_user)):
    return {
        'username': user['name']
    }