# main.py

import redis
import json
import hashlib
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# lazy logging
logger.info('Starting the FastAPI application...')

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Load the pre-trained model
model = joblib.load('model.joblib')

# Define the input data model
class IrisFlower(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    # Helper function to convert to list
    def to_list(self):
        return [
            self.SepalLengthCm, 
            self.SepalWidthCm, 
            self.PetalLengthCm, 
            self.PetalWidthCm
        ]
    

    # Helper function to create a unique cache key
    def cache_key(self):
        # Create a unique cache key based on the input features
        raw = json.dumps(self.model_dump(), sort_keys=True)
        return f"Preduct: {hashlib.sha256(raw.encode()).hexdigest()}"

# Prediction endpoint with caching
@app.post('/predict')
async def predict(data: IrisFlower): # Input data
    key = data.cache_key()
    cached_result = redis_client.get(key) # Check cache

    if cached_result:
        logger.info('Cache hit')
        print("Serving prediction from cache!")
        return json.loads(cached_result) # Return cached result
    
    # Cache miss, compute prediction
    prediction = model.predict([data.to_list()])[0] # Make prediction; get first element
    result = {'prediction': int(prediction)} # Prepare result (Serialize numpy int to native int)
    redis_client.set(key, json.dumps(result), ex=3600) # Store in cache; expire in 1 hour
    logger.info('Cache miss - computed prediction')
    return result # Return new prediction 