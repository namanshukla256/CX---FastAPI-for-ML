<<<<<<< HEAD
import models, schemas, crud

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session. Session for Operations
def get_db():
    db = SessionLocal() # sessionmaker 
    try:
        yield db # Generator = Returns the database session 
    finally:
        db.close()

############
# Endpoints #
############

# 1. Create an employee
@app.post("/employees", response_model = schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee) # Directly use from crud


# 2. Get all employees
@app.get("/employees", response_model = List[schemas.EmployeeOut]) # List of employees
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


# 3. Get a specific employee
@app.get("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


# 4. Update an employee
@app.put("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


# 5. Delete an employee
@app.delete("/employees/{emp_id}", response_model=dict) # OR response_model = schemas.EmployeeOut
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # return employee
    return {
        'message': 'Employee deleted successfully'
    }
=======
# main.py

>>>>>>> 7709fed302fd06d2836e644253d50f5764308f48
