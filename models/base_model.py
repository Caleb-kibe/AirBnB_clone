#!/usr/bin/python3
"""Defines a class BaseModel"""
from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """Represents BaseModel of the Hbnb applicaion"""
    def __init__(self, *args, **kwargs):
        """Definition of the constructor
        Args:
            *Args: Not used
            **Kwargs (dict): key/value pairs of the attributes
        """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    kwargs[k] = datetime.strptime(v, time_form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts the object into a dictionary representation"""
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """Defines how the object will be
        displayed when printed as a string"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
