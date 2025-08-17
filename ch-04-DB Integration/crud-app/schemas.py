# schemas.py

"""
Defines the Pydantic schemas for the CRUD application. For data validation and serialization.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    # This will override the email field to make it optional during creation
    # Also provides flexibility in the creation process
    email: Optional[EmailStr] = None  # Optional for creation


class EmployeeUpdate(EmployeeBase):
    email: Optional[EmailStr] = None  # Optional for updates

class EmployeeOut(EmployeeBase):
    # Data sharing of employee information  
    id: int

# OR
# class EmployeeInDB(EmployeeBase):
#     id: int


    # Config: SQLAlchemy expects to serialize the data
    # At the time of reading data from the database
    # Smooth conversion between Pydantic models and SQLAlchemy models -> JSON
    # Defined within the EmployeeOut class only
    class Config:
        orm_mode = True


