#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle width, height and position

    Attributes:
        width(int): The width of theRectangle
        height(int): The height of the Rectangle
        x(int): The x-coordinate of the Rectangle's position
        y(int): The y-coordinate of the Rectangle's position
        id(int): The unique identifier for the Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle intance.
        Args:
            width(int): The width of theRectangle
            height(int): The height of the Rectangle
            x(int): The x-coordinate of the Rectangle's position. Default is 0.
            y(int): The y-coordinate of the Rectangle's position. Default is 0.
            id(int): The unique identifier for the Rectangle. Default is None.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Get the width of the rectangle."""
        return self.__width

    @setter
    def width(self, value):
        """Set the width of the rectangle.

            Args:
                value(int): The width value to set

            Raises:
                ValueError: If the width is not a positive number
                TypeError: if the type is not an integer
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("value must be > than 0")
        self.__width = value

    @property
    def height(self):
        """int: Get the height of the rectangle."""
        return self.__height

    @setter
    def height(self, value):
        """Set the height of the rectangle.

            Args:
                value(int): The height value to set

            Raises:
                ValueError: If the height is not a positive number
                TypeError: if the type is not an integer
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: Get the x-coordinate of the rectangle's position."""
        return self.__x

    @setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position.

            Args:
                value (int): The x-coordinate value to set.

            Raises:
                ValueError: If the width is not a positive number
                TypeError: if the type is not an integer
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: Get the y-coordinate of the rectangle's position."""
        return self.__y

    @setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position.

            Args:
                value (int): The y-coordinate value to set.

            Raises:
                ValueError: If the width is not a positive number
                TypeError: if the type is not an integer
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__y = value
