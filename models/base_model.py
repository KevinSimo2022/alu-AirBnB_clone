#!/usr/bin/python3
""" this is the base class for all models """
import uuid
from datetime import date, datetime, time
from models import storage


class BaseModel:
    """class defining commom attributes
    for other classes"""

    def __init__(self, *argv, **kwargs):
        """ instance attributes
        id : string
        created_at: datetime
        updated_at: datetime

        getting arguments to recreate
        BaseModel
        creates new instance Model
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        temp_dict = self.__dict__
                        temp_dict[key] = \
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        temp_dict = self.__dict__
                        temp_dict[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ default string output of class name \
                ,id and dictionary files """
        return '[{}] ({}) {}'\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        update of attribute updated_at
        with latest time
        updated_at: datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        get the objects of the instance
        returns: dictionary
        """
        temp_dict = self.__dict__.copy()
        temp_dict['__class__'] = self.__class__.__name__
        temp_dict['created_at'] = temp_dict['created_at'].isoformat()
        temp_dict['updated_at'] = temp_dict['updated_at'].isoformat()
        return temp_dict
