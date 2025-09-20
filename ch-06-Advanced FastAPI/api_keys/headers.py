# headers.py

from fastapi import FastAPI,Depends, HTTPException, Header

app = FastAPI()

API_KEY = 'mysecretapikey' # Predefined API key for simplicity

# Dependency to get and validate API key from headers
def get_api_key(api_key: str = Header(...)): # Expecting 'api_key' header
    if api_key != API_KEY: # Validate API key
        raise HTTPException(status_code=403, detail='Could not validate API key') # Raise 403 if invalid
    return api_key # Return valid API key

# Protected endpoint that requires a valid API key
@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {
        'data': 'This is some protected data'
    } # Return protected data if API key is valid

@app.get('/')
def read_root():
    return {'message': 'Welcome to the API!'}