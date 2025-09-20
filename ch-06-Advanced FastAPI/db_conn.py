from fastapi import FastAPI, Depends

app = FastAPI()

# Dependency function to simulate a database connection
def get_db():
    db = {'connection': 'mock_db_connection'}
    try:
        yield db # Simulate opening a database connection
    finally:
        pass # Simulate closing the database connection

# Endpoint that uses the database connection dependency
@app.get("/home")
def home(db=Depends(get_db)): # Dependency injection
    return {'db_status': db['connection']} # Use the db connection