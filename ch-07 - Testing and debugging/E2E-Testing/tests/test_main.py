# tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_eligibility_pass():
    response = client.post(
        '/loan-eligibility',
        json={
            'income': 60000,
            'age': 30,
            'employment_status': 'employed'
        }
    )
    assert response.status_code == 200
    assert response.json() == {"eligible": True}


def test_eligibility_fail():
    response = client.post(
        '/loan-eligibility',
        json={
            'income': 30000,
            'age': 18,
            'employment_status': 'unemployed'
        }
    )
    assert response.status_code == 200
    assert response.json() == {"eligible": False}


"""
pytest tests/
============================================== test session starts ==============================================
platform linux -- Python 3.11.7, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/naman/Downloads/MyCode/CX---FastAPI-for-ML/ch-07 - Testing and debugging/E2E-Testing
plugins: anyio-4.10.0
collected 2 items                                                                                               

tests/test_main.py ..                                                                                     [100%]

=============================================== 2 passed in 0.60s ===============================================
"""