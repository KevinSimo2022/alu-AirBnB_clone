#!/usr/bin/python3

import json
from os.path import exists


class FileStorage:
<<<<<<< HEAD
        """ file storage class"""

=======
>>>>>>> 11d73330625703ad328d10093108563625181f3f
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj._class.__name_, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
<<<<<<< HEAD
        """ deserializes JSON from the file """
    from models.base_model import BaseModel
    from models.user import User
    from models.city import City
    from models.state import State
    from models.place import Place
    from models.review import Review
    from models.amenity import Amenity
    
    class_mapping = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'State': State,
        'Place': Place,
        'Review': Review,
        'Amenity': Amenity
    }
    
    if path.exists(self.__file_path):
        with open(self.__file_path, "r", encoding='utf-8') as in_file:
            dataset = json.load(in_file)
            for data in dataset.values():
                class_name = data.get('__class__')
                if class_name in class_mapping:
                    class_instance = class_mapping[class_name](**data)
                    self.new(class_instance)
                else:
                    print(f"Warning: Unknown class '{class_name}' in JSON data.")
=======
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file does not exist,
        no exception should be raised).
        """
        if exists(self.__file_path) is False:
            return

        from .class_objects import classes
        
        
        with open(FileStorage.__file_path, 'r') as file:
            data = json.load(file)
            for key, obj_data in data.items():
                class_name, obj_id = key.split('.')
                obj_class = classes[class_name]
                obj_instance = obj_class(**obj_data)
                FileStorage.__objects[key] = obj_instance
>>>>>>> 11d73330625703ad328d10093108563625181f3f
