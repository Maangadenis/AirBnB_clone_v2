#!/usr/bin/python3
""" Defines a base class for all models in our hbnb clone """
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """ A base class for all hbnb models """
    id = Column(String(60), unique=True, nullable=False,
                primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Instantiates a new model """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key not in ('__class__', '_sa_instance_state'):
                    setattr(self, key, value)
            if not self.id:
                self.id = str(uuid.uuid4())
            timestamp = datetime.now()
            if 'created_at' not in kwargs:
                self.created_at = timestamp
            if 'updated_at' not in kwargs:
                self.updated_at = timestamp

    def __str__(self):
        """ Returns a string representation of the instance """
        print_dict = self.__dict__.copy()
        if '_sa_instance_state' in print_dict:
            del print_dict['_sa_instance_state']
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, print_dict)

    def save(self):
        """ Updates updated_at with current time when instance is changed """
        from . import storage  # here instead of top to avoid circular import
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Convert instance into dict format """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """ Delete current instance storage """
        from . import storage  # here instead of top to avoid circular import
        storage.delete(self)
