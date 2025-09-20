from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware # Import GZipMiddleware

# GZipMiddleware
"""
GZipMiddleware Explanation with analogy:
- A GZipMiddleware is a middleware that compresses the response body of an HTTP request.
- It does this by wrapping the response body in a gzip file and then sending it to the client.
- The client can then decompress the response body using the gzip file. 
"""

app = FastAPI()

app.add_middleware(
    GZipMiddleware, minimum_size=1000  # Only compress responses larger than 1000 bytes
)