#!/usr/bin/python3
'''
a new class of Rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''
        Respresent a class Rectangle inherits from Base
        Args:
            id: public attribute
            width: width of Rectangle
            height: height o rectangle
            x
            y
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            instantiation of new instance of Rectangle class
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
        method property to get the attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        method setter to set the value
        '''
        Rectangle.checking("width", value)
        self.__width = value

    @property
    def height(self):
        '''
        method property to get the attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        method setter to set the value
        '''
        Rectangle.checking("height", value)
        self.__height = value

    @property
    def x(self):
        '''
        method property to get the attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        method setter to set the value
        '''
        Rectangle.checking("x", value)
        self.__x = value

    @property
    def y(self):
        '''
        method property to get the attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        method setter to set the value
        '''
        Rectangle.checking("y", value)
        self.__y = value

    @staticmethod
    def checking(name, value):
        '''
        static method for handle the raise exceptions
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''
        returns the area of the Rectangle Class
        '''
        return self.height * self.width

    def display(self):
        '''
        prints in stdout the Rectangle instance with the character #
        '''
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)
