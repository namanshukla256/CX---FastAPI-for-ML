# config.py

from fastapi import FastAPI, Depends

app = FastAPI()

# Settings class to hold configuration
class Settings:
    def __init__(self):
        self.api_key = 'my_secret'
        self.debug = True

# Dependency to retrieve settings
def get_settings():
    return Settings()

# Endpoint to retrieve configuration
@app.get("/config")
def get_config(settings: Settings = Depends(get_settings)):
    return {
        'api_key': settings.api_key
    }