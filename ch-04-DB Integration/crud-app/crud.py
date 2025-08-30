# crud.py

"""
CRUD operations for the Employee model. Business logic for handling employee data.
"""

from sqlalchemy.orm import Session
import models, schemas


# Functions for CRUD operations
def get_employees(db: Session):
    return db.query(models.Employee).all() # Query to Retrieve all employees from the Employee table


def get_employee(db: Session, emp_id: int):
    return (
        db
        .query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    ) # We Query from the Employee table, apply filter to get the employee with the given emp_id, and return the first result


def create_employee(db: Session, employee: schemas.EmployeeCreate): # we need an Eployee to create a new employee
    db_employee = models.Employee(
        name = employee.name,
        email = employee.email
    ) # Create a new Employee instance with the provided name and email
    db.add(db_employee) # Add the new employee to the session. This will change the state of the instance to "pending" in the session
    db.commit() # Commit the session to save the new employee to the database. When we commit, the state of the instance changes to "persistent" in the session
    db.refresh(db_employee) # Refresh the instance to get the updated data from the database. Generates a new ID for the employee.
    return db_employee # Return the newly created employee instance


def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeUpdate):
    # Retrieve the employee to be updated
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        # Update the employee's attributes
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee) # Refresh the instance to get the updated data from the database
        # Else if the employee does not exist, we can raise an exception or return None
    return db_employee # Return the updated employee instance


def delete_employee(db: Session, emp_id: int):
    # Retrieve the employee to be deleted
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit() # Commit the session to delete the employee from the database. No need to refresh the instance as it will be removed from the session
    return db_employee  # Return the deleted employee instance or None if not found