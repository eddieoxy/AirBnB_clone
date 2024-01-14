Project Description
This project is an implementation of a command-line interpreter for managing instances of various classes in a simulated Airbnb clone. It uses a custom command interpreter to interact with and manipulate instances of classes such as BaseModel, User, State, City, Amenity, Place, and Review. The instances are stored and retrieved from a JSON file using serialization and deserialization.

Command Interpreter
The command interpreter, implemented in console.py, provides the following functionalities:

create: Creates a new instance of BaseModel, saves it to the JSON file, and prints the id.

show: Prints the string representation of an instance based on the class name and id.

destroy: Deletes an instance based on the class name and id, saving the change into the JSON file.

all: Prints all string representations of instances based on the class name.

update: Updates an instance based on the class name and id by adding or updating attributes, saving the change into the JSON file.

Other basic commands such as quit and EOF are also available.

How to Start
To start the command interpreter, run the console.py script. This will launch the interpreter with the prompt (hbnb).

$ ./console.py
How to Use
The command interpreter supports various commands to interact with the instances. Here are some examples:

Creating a new instance:

(hbnb) create BaseModel
Showing an instance:

(hbnb) show BaseModel 1234-1234-1234
Destroying an instance:

(hbnb) destroy BaseModel 1234-1234-1234
Listing all instances:

(hbnb) all BaseModel
Updating an instance:

(hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
Exiting the command interpreter:

(hbnb) quit
Authors
[BANAMBO EDMOND]

Notes
All files, classes, and func
