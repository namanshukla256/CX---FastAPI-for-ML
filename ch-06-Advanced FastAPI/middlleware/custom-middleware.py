import time
from fastapi import FastAPI, Request

# Import basic class for custom middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# Create custom middleware class
class TimerMiddleware(BaseHTTPMiddleware):
    # Define async dispatch method
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)

        # call_next is a function that receives a request and returns a response
        # Why use async/await -> non-blocking I/O operations

        duration = time.time() - start_time
        print(f"Request: {request.url.path} processed in {duration:.5f} seconds")

        return response


# Add middleware to the app
app.add_middleware(TimerMiddleware)

@app.get("/hello")
async def hello():
    for _ in range(1000000):
        pass # Simulate a time-consuming task
    return {"message": "Hello, World!"}
