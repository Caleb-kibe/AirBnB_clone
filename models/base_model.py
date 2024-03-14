#!/usr/bin/python3
"""Defines a class BaseModel"""
from datetime import datetime
import uuid


class BaseModel:
    """Represents BaseModel of the Hbnb applicaion"""
    def __init__(self, *args, **kwargs):
        """Definition of the constructor
        Args:
            *Args: Not used
            **Kwargs (dict): key/value pairs of the attributes
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    kwargs[k] = datetime.fromisoformat(v)

            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """Defines how the object will be
        displayed when printed as a string"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Converts the object into a dictionary representation"""
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = data["created_at"]
        data["updated_at"] = data["updated_at"]
        return {k: v.isoformat() if isinstance(v, datetime)
                else v for k, v in data.items()}
