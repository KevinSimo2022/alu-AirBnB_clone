#!/usr/bin/python3
"""Defines BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base Model Class

    This class defines common attributes and methods for other classes.

    Attributes:
        id (str): A unique identifier generated with UUID.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime of the last update to the instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], datetime_format)
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], datetime_format)
            del kwargs["__class__"]
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Update the `updated_at` attribute with the current datetime
        and save the changes.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing the object's attributes.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: A formatted string containing class name, ID, and attributes.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
