#!/usr/bin/python3
"""Defines a class Base"""
import json
import os.path
import csv
import turtle


class Base:
    """Class that defines properties of Base.

     Attributes:
        id (int): Identity of each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Creates new instances of Base.

        Args:
            id (int, optional): Identity of each instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances to save.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        data = []

        if list_objs is not None:
            for obj in list_objs:
                data.append(obj.to_dictionary())

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(data))

    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string to convert.

        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary.

        Args:
            dictionary (dict): A dictionary containing attribute values.

        Returns:
            instance: An instance with attributes set based on the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: A list of instances based on the data from the JSON file.
        """
        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, 'r') as file:
                data = file.read()
                if data:
                    dictionaries = cls.from_json_string(data)
                    for dictionary in dictionaries:
                        instance = cls.create(**dictionary)
                        instances.append(instance)
        except FileNotFoundError:
            pass  # If the file doesn't exist, return an empty list

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of rectangles or squares in csv.

        Args:
            cls (any): class.
            list_objs (list): objects.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ == "Square":
                for i in list_objs:
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of rectangles or squares in csv.

        Args:
            cls (any): class.
        """
        filename = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except(Exception):
            pass
        return(my_obj)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics."""
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")

        # Create a Turtle object for drawing
        pen = turtle.Turtle()
        pen.speed(1)  # Set the drawing speed (adjust as needed)

        # Draw rectangles
        for rectangle in list_rectangles:
            pen.penup()  # Lift the pen to move without drawing
            pen.goto(rectangle.x, rectangle.y)  # Move to the starting position
            pen.pendown()  # Lower the pen to start drawing
            pen.color("blue")  # Set the color (you can change it)

            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)
            pen.penup()  # Lift the pen after drawing the rectangle

        # Draw squares
        for square in list_squares:
            pen.penup()  # Lift the pen to move without drawing
            pen.goto(square.x, square.y)  # Move to the starting position
            pen.pendown()  # Lower the pen to start drawing
            pen.color("red")  # Set the color (you can change it)

            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

            pen.penup()  # Lift the pen after drawing the square

        # Close the Turtle graphics window when clicked
        screen.exitonclick()
