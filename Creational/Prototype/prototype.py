import copy
from abc import ABC, abstractmethod


# Prototype Interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


# Concrete Prototype Classes
class Circle(Prototype):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def __str__(self):
        return f"Circle(radius={self.radius}, color={self.color})"

    def clone(self):
        return copy.deepcopy(self)


class Rectangle(Prototype):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color={self.color})"

    def clone(self):
        return copy.deepcopy(self)


# Client Code
if __name__ == "__main__":
    # Original Objects
    circle1 = Circle(radius=5, color="Red")
    rectangle1 = Rectangle(width=10, height=20, color="Blue")

    print("Original Objects:")
    print(circle1)  # Circle(radius=5, color=Red)
    print(rectangle1)  # Rectangle(width=10, height=20, color=Blue)

    # Cloning
    circle2 = circle1.clone()
    rectangle2 = rectangle1.clone()

    print("\nCloned Objects:")
    print(circle2)  # Circle(radius=5, color=Red)
    print(rectangle2)  # Rectangle(width=10, height=20, color=Blue)

    # Modifying Cloned Objects
    circle2.color = "Green"
    rectangle2.width = 15

    print("\nAfter Modifications:")
    print(f"Original Circle: {circle1}")  # Circle(radius=5, color=Red)
    print(f"Cloned Circle: {circle2}")  # Circle(radius=5, color=Green)
    print(f"Original Rectangle: {rectangle1}")  # Rectangle(width=10, height=20, color=Blue)
    print(f"Cloned Rectangle: {rectangle2}")  # Rectangle(width=15, height=20, color=Blue)
