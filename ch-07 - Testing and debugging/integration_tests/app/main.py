# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from app.logic import is_eligible_for_loan

app = FastAPI()

# Defining Pydantic data model
class Applicant(BaseModel):
    income: float
    age: int
    employment_status: str


# Defining Endpoints - Send the data of applicant
@app.post("/loan-eligibility")
def check_eligibility(applicant: Applicant):
    eligibility = is_eligible_for_loan(
        income = applicant.income,
        age = applicant.age,
        employment_status = applicant.employment_status
    ) # Calling the logic function
    return {"eligible": eligibility}