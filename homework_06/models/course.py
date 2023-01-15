from sqlalchemy import Column, String, Integer
from .database import db


class Course(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    duration = Column(Integer, nullable=False)
