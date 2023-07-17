#!/usr/bin/python3
"""
module contains class `Rectangle`
"""
from models.base import Base as BaseClass


class Rectangle(BaseClass):
    """
    defines a Rectangle that inherits from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """
        initialize Rectangle instance
        Args:
            @width: width of the Rectangle
            @height: heightof the rectangle
            @x, @y
       """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method for height attribute
        return:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        getter method for x attribute
        return:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x attribute"""
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter method for y attribute
        return:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y attribute"""
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """print rectangle instance to stdout using `#`"""
        for _ in range(self.__y):
            print("")
        for h in range(self.__height):
            print(" " * self.__x, end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """
        return:
            [Rectangle] (id) <x>/<y> - <width>/<height>
        """
        return (
                f"[{self.__class__.__name__}]"
                f" ({self.id}) {self.__x}/{self.__y}"
                f" - {self.__width}/{self.__height}"
                )

    def update(self, *args, **kwargs):
        """
        updates rectangle instance
        Args:
            @*args: (int)
            Assigns an argument to each attribute
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        arg_counter = 0
        for arg in args:
            if arg_counter == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
            elif arg_counter == 1:
                self.__width = arg
            elif arg_counter == 2:
                self.__height = arg
            elif arg_counter == 3:
                self.__x = arg
            elif arg_counter == 4:
                self.__y = arg
            arg_counter += 1

        for key, value in kwargs.items():
            arg_names = ["id", "width", "height", "x", "y"]
            if key in arg_names and arg_names.index(key) >= arg_counter:
                if key == arg_names[0]:
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == arg_names[1]:
                    self.__width = value
                elif key == arg_names[2]:
                    self.__height = value
                elif key == arg_names[3]:
                    self.__x = value
                elif key == arg_names[4]:
                    self.__y = value

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
