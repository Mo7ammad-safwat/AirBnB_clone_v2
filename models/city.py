#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, DateTime, String
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """ """
    __tablename__ = "cities"

    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
