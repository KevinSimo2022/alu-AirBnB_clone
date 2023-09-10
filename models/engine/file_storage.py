#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
                for key, value in new_obj_dict.items():
                    class_name = value['__class__']
                    new_instance = eval(class_name)(**value)
                    self.__objects[key] = new_instance
        except FileNotFoundError:
            pass
