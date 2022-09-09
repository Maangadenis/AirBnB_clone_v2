#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of models currently in storage, or all of
        one type.

        Args:
            cls (BaseModel-derived): class of object to list

        Returns:
            all_of_class (dict): dictionary of all objects in file storage
                of class `cls`.
        """
        if cls is None:
            return self.__objects
        else:
            all_of_class = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    all_of_class[key] = value
            return all_of_class

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete an object if it exists"""
        try:
            if obj:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                del self.__objects[key]
        except:
            pass

    def close(self):
        """ File storage equivalent to `DBStorage.close()`, resets current
        `storage` by reloading JSON file.

        Project: 0x04. AirBnB clone - Web framework
        Task: 7. Improve engines
        """
        self.reload()
