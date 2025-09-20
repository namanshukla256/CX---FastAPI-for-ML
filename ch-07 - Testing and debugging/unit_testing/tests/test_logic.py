# tests/test_logic.py

import pytest
from app.logic import is_eligible_for_loan

def test_eligible_user():
    assert is_eligible_for_loan(60000, 25, 'employed') == True

def test_underage_user():
    assert is_eligible_for_loan(60000, 18, 'employed') == False

def test_low_income():
    assert is_eligible_for_loan(40000, 30, 'employed') == False

def test_unemployed_user():
    assert is_eligible_for_loan(65000, 30, 'unemployed') == False

# Just at the border as defined in logic
def test_boundary_user():
    assert is_eligible_for_loan(50000, 21, 'employed') == True


"""
pytest tests/test_logic.py 
================================== test session starts ===================================
platform linux -- Python 3.11.7, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/naman/Downloads/MyCode/CX---FastAPI-for-ML/ch-07 - Testing and debugging/unit_testing
plugins: anyio-4.10.0
collected 5 items                                                                        

tests/test_logic.py .....                                                          [100%]

=================================== 5 passed in 0.01s ===================================
"""