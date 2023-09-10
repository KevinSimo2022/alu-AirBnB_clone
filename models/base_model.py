#!/usr/bin/python3
""" This is the base class for all models """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ Class defining common attributes for other classes """

    def __init__(self, *args, **kwargs):
        """ Initialize instance attributes:
            - id (string)
            - created_at (datetime)
            - updated_at (datetime)

            Args:
                args: Not used in this constructor.
                kwargs: Dictionary of attributes to recreate BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ Default string representation of the class """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the 'updated_at' attribute with the current time """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Get the dictionary representation of the object """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict
