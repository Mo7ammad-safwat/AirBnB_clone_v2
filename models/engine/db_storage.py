#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """SQL database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """ """
        userName = getenv("HBNB_MYSQL_USER")
        paswd = getenv("HBNB_MYSQL_PWD")
        hostName = getenv("HBNB_MYSQL_HOST")
        dbNam = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(userName, paswd, hostName, dbNam),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for clase in classes:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """Add obj to database session."""
        self.__session.add(obj)

    def save(self):
        """save the changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from db session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ """
        Base.metadata.create_all(self.__engine)
        tmp_session = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
        Session = scoped_session(tmp_session)
        self.__session = Session()
