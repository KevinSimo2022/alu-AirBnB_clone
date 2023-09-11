#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Add an object to the current database."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file."""
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserialize JSON file to __objects."""
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
                for key, value in new_obj_dict.items():
                    class_name = value['__class__']
                    new_instance = eval(class_name)(**value)
                    self.__objects[key] = new_instance
        except FileNotFoundError:
            pass
