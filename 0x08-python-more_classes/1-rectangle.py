#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """Representation of a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """property retriever"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property retriever"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

