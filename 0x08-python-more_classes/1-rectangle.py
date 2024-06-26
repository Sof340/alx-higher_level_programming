#!/usr/bin/python3
"""
A class representing a rectangle.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width: private, depecting the width of the rectangle.
        heigth: private, depecting the heigth of the rectangle.

    Methods:
        width(self): retrieves the private attribute width.
        width(self, width): sets the private attribute width.
        height(self): retrieves the private attribute height.
        height(self, height): sets the private attribute height.
    """
    def __init__(self, width=0, height=0):
        """
        initializes the private attributes.
        """
        try:
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            elif not isinstance(height, int):
                raise TypeError("height must be an integer")
            elif (height < 0):
                raise ValueError("height must be >= 0")
            elif (width < 0):
                raise ValueError("width must be >= 0")
            else:
                self.__width = width
                self.__height = height
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    @property
    def width(self):
        """ retrives the private attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of the private attribute width """
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif (value < 0):
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    @property
    def height(self):
        """ retrives the private attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of the private attribute height """
        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif (value < 0):
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
