#!/usr/bin/python3
'''Module for Rectangle class.'''


class Rectangle:
    '''
    This class defines a simple Rectangle.
    '''

    def __init__(self, width=0, height=0):
        '''
        Constructor.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Property for the width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Property for the height of the rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Printable string of a rectangle"""
        str = ""
        if self.__width != 0 and self.__height != 0:
            str += "\n".join("#" * self.__width
                             for j in range(self.__height))
        return str

    def __repr__(self):
        '''Returns string representation...'''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        '''Called at instance deletion.'''
        print("Bye rectangle...")
