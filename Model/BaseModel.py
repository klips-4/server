import datetime
from typing import List

from sqlalchemy import Column, Integer, DateTime

from app import db, engine
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class BaseModel(db.Model):
    __abstract__ = True
    session = engine.session

    id = Column(Integer, primary_key=True)


