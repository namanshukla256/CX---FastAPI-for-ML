# tests/test_main.py

from fastapi.testclient import TestClient # Use Testclient to make Test Application
from app.main import app

client = TestClient(app) # FastAPI app

# Two cases (Eligible and not eligible)

# Test case for eligible
def test_eligibility_pass():
    payload = {
        'income': 60000,
        'age': 30,
        'employment_status': 'employed'
    } # Define the data payload

    response = client.post('/loan-eligibility', json=payload) # Now hit the endpoint using Testclient
    
    # post returns a response thats why we need to check the response
    assert response.status_code == 200 # Check if the response is OK
    assert response.json() == {"eligible": True} # Check if the response is as expected


# Test case for not eligible
def test_eligibility_fail():
    payload = {
        'income': 30000,
        'age': 18,
        'employment_status': 'unemployed'
    }

    response = client.post('/loan-eligibility', json=payload)
    assert response.status_code == 200
    assert response.json() == {"eligible": False}


"""
tests$ pytest tes
ts/
====================== test session starts ======================
platform linux -- Python 3.11.7, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/naman/Downloads/MyCode/CX---FastAPI-for-ML/ch-07 - Testing and debugging/integration_tests
plugins: anyio-4.10.0
collected 2 items                                               

tests/test_main.py ..                                     [100%]

======================= 2 passed in 0.33s =======================
"""