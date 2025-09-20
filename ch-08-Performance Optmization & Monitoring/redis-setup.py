import redis

r = redis.Redis(host='localhost', port=6379, db=0) # Connect to Redis server. db=0 is the default database

# Test the connection
try:
    if r.ping():
        print("Connected to Redis server successfully!")
except redis.ConnectionError:
    print("Failed to connect to Redis server.")

# Example usage
r.set('framework', 'FastAPI') # Set a key-value pair in Redis

value = r.get('framework') # Get the value for the key 'framework'

# Decode bytes to string and print the value
print(f"Stored value for framework:{value.decode()}")


"""
Connected to Redis server successfully!
Stored value for framework:FastAPI
"""











































































































