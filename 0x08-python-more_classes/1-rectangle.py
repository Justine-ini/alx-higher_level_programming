#!/usr/bin/python3
"""Creating a rectangle class."""


class Rectangle:
    """A class to represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height = height

    @heightsetter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(height, value):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
