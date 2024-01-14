#!/usr/bin/python3
"""create a console that contains
    a command interpreter"""

import cmd
import json
import re
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(arg):
    """Exatact specific parts of a string based on {} nd []"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexr = split(arg[:brackets.span()[0]])
            substr_list = [i.strip(",") for i in lexer]
            substr_list.append(brackets.group())
            return substr_list
    else:
        lexr = split(arg[:curly_braces.span()[0]])
        substr_list = [i.strip(",") for i in lexr]
        substr_list.append(curly_braces.group())
        return substr_list


class HBNBCommand(cmd.Cmd):
    """a command class that inherits from cmd"""
    prompt = '(hbnb) '
    __classes = {"BaseModel", "User", "State", "City", "Place",
                 "Amenity", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF exits the program"""
        print("")
        return True

    def emptyline(self):
        """execute nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        cls = parse(arg)
        if len(cls) == 0:
            print("** class name missing **")
        elif cls[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            # Update attribute names here
            print(eval(cls[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        cls = parse(arg)
        o_dict = storage.all()
        if len(cls) == 0:
            print("** class name missing **")
        elif cls[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(cls) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(cls[0], cls[1]) not in o_dict:
            print("** no instance found **")
        else:
            print(o_dict["{}.{}".format(cls[0], cls[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        cls = parse(arg)
        o_dict = storage.all()
        if len(cls) == 0:
            print("** class name missing **")
        elif cls[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(cls) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(cls[0], cls[1]) not in o_dict.keys():
            print("** no instance found **")
        else:
            del o_dict["{}.{}".format(cls[0], cls[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        cls = parse(arg)
        if len(cls) > 0 and cls[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(cls) > 0 and cls[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(cls) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        cls = parse(arg)
        o_dict = storage.all()

        if len(cls) == 0:
            print("** class name missing **")
            return False
        if cls[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(cls) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(cls[0], cls[1]) not in o_dict.keys():
            print("** no instance found **")
            return False
        if len(cls) == 2:
            print("** attribute name missing **")
            return False
        if len(cls) == 3:
            try:
                type(eval(cls[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(cls) == 4:
            obj = o_dict["{}.{}".format(cls[0], cls[1])]
            if cls[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[cls[2]])
                obj.__dict__[cls[2]] = valtype(cls[3])
            else:
                obj.__dict__[cls[2]] = cls[3]
        elif type(eval(cls[2])) == dict:
            obj = o_dict["{}.{}".format(cls[0], cls[1])]
            for k, v in eval(cls[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def default(self, arg):
        """Catch commands if nothing else matches"""
        arg_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }
        match = re.search(r"\.", arg)
        if match is not None:
            cls = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", cls[1])
            if match is not None:
                command = [cls[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(cls[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Counts the instances of a class"""
        cls = parse(arg)
        count = 0
        for obj in storage.all().values():
            if cls[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
