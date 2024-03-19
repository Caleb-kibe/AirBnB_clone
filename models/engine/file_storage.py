#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        name_obj = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name_obj, obj.id)] = obj

    def save(self):
        dict_obj = FileStorage.__objects
        o_dict = {obj: dict_obj[obj].to_dict() for obj in dict_obj.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(o_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                o_dict = json.load(file)
                for ob in o_dict.values():
                    class_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(class_name)(**ob))
        except FileNotFoundError:
            return
