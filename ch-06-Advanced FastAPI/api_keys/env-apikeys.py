from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic_settings import BaseSettings

# Define settings to load environment variables
class Settings(BaseSettings):
    api_key: str

    class Config:
        env_file = '.env'  # Load environment variables from .env file
        env_file_encoding = 'utf-8'

settings = Settings()  # Create settings instance to access environment variables
app = FastAPI()

# Dependency to get and validate API key from headers
def get_api_key(api_key: str = Header(...)):
    if api_key != settings.api_key: # Validate API key against environment variable
        raise HTTPException(status_code=403, detail='Could not validate API key')
    return api_key

# Protected endpoint that requires a valid API key
@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {
        'data': 'This is some protected data'
    } # Return protected data if API key is valid

@app.get('/')
def read_root():
    return {'message': 'Welcome to the API!'}