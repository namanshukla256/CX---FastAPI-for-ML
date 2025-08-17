# models.py

"""
Database models for the CRUD application using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from database import Base

# Define the Employee model = Table
class Employee(Base):
    __tablename__ = "employees"

    # Define the table columns (Fields)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)