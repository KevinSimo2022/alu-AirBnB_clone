#!/usr/bin/python3
import cmd
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    class_list = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            obj = eval(line)()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            line_list = line.split(" ")
            if len(line_list) == 1:
                print("** instance id missing **")
            else:
                storage = FileStorage()
                obj_dict = storage.all()
                key = "{}.{}".format(line, line_list[1])
                if key in obj_dict:
                    print(obj_dict[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            line_list = line.split(" ")
            if len(line_list) == 1:
                print("** instance id missing **")
            else:
                storage = FileStorage()
                obj_dict = storage.all()
                key = "{}.{}".format(line, line_list[1])
                if key in obj_dict:
                    del obj_dict[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        obj_list = []
        storage = FileStorage()
        obj_dict = storage.all()
        if not line:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif line in self.class_list:
            for key, val in obj_dict.items():
                if line in key:
                    obj_list.append(str(val))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            storage = FileStorage()
            obj_dict = storage.all()
            line_list = line.split(" ")
            if len(line_list) == 1:
                print("** instance id missing **")
            elif line_list[1] not in obj_dict:
                print("** no instance found **")
            elif len(line_list) == 2:
                print("** attribute name missing **")
            elif len(line_list) == 3:
                print("** value missing **")
            else:
                obj = obj_dict[line_list[1]]
                setattr(obj, line_list[2], line_list[3])
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

