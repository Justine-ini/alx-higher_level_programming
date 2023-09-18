#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""


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
            raise ValueError("width must be > than 0")
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
            raise ValueError("height must be > 0")
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
        if value <= 0:
            raise ValueError("x must be >= 0")
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
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of a rectangle

        Returns:
            int: The area of a rectangl.
        """
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
