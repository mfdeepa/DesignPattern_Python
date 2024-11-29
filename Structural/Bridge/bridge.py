from abc import ABC, abstractmethod


# Implementor Interface
class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass


# Concrete Implementors
class RedColor(Color):
    def apply_color(self):
        return "Red"


class BlueColor(Color):
    def apply_color(self):
        return "Blue"


# Abstraction
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


# Refined Abstractions
class Circle(Shape):
    def draw(self):
        return f"Circle filled with {self.color.apply_color()} color"


class Square(Shape):
    def draw(self):
        return f"Square filled with {self.color.apply_color()} color"


# Client Code
if __name__ == "__main__":
    red = RedColor()
    blue = BlueColor()

    circle = Circle(red)
    print(circle.draw())  # Output: Circle filled with Red color

    square = Square(blue)
    print(square.draw())  # Output: Square filled with Blue color

    # Changing the color implementation
    circle_blue = Circle(blue)
    print(circle_blue.draw())  # Output: Circle filled with Blue color
