import datetime
import json
from typing import List

from sqlalchemy import Column, Integer, DateTime

from app import db, engine
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class BaseModel(db.Model):
    __abstract__ = True
    session = engine.session

    _guarder: List[str] = []
    _fillable: List[str] = []
    _manual_fillable: List[str] = []

    id = Column(Integer, primary_key=True)
