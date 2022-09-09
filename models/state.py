#!/usr/bin/python3
""" 0x02. AirBnB clone - MySQL, task 6. DBStorage - States and Cities """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .city import City
from .base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """Defines attributes for `State` as it inherits from `BaseModel`,
    and ORM properties in relation to table `states`.
    Attributes:
        name (Column): name of state, string of max 128 chars
        cities (relationship): one-to-many-association to `City`
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Getter for list of all `City` objects when in file storage
            mode.
            """
            from . import storage
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
