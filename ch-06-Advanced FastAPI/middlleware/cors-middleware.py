from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Intention is to inject this middleware to allow CORS requests from any origin

app.add_middleware(
    # Allow all origins
    CORSMiddleware,
    allow_origins=[
        'https://my-frontend.com',
        'http://localhost:3000',
    ], # List of allowed origins
    allow_credentials=True, # Allow cookies and credentials
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'], # Allow all HTTP methods
    allow_headers=["*"], # Allow all headers
)

# Define endpoints
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: dict):
    return item