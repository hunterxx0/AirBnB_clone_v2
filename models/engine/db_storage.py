#!/usr/bin/python3
""" Module """

from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ class """

    __engine = None
    __session = None
    cl = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if (getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ yo """

        res = {}
        if not cls:
            for c in self.cl.keys():
                q = self.__session.query(self.cl[c]).all()
                if q:
                    for x in q:
                        res[c + '.' + x.id] = x

        else:
            q = self.__session.query(self.cl[cls]).all()
            if q:
                for x in q:
                    res[cls + '.' + x.id] = x

        return res

    def new(self, obj):
        """ new """

        self.__session.add(obj)

    def save(self):
        """ save """

        self.__session.commit()

    def delete(self, obj=None):
        """ delete """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload """

        Base.metadata.create_all(self.__engine)
        sf = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sf)()

    def close(self):
        """ Call remove() method on the private session attribute """
        self.__session.remove()
