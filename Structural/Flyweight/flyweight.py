from abc import ABC, abstractmethod


# Flyweight Class (Intrinsic State)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


# Concrete Flyweight Class
class Circle(Shape):
    def __init__(self, color):
        self.color = color  # The intrinsic state (shared between objects)

    def draw(self):
        print(f"Drawing a {self.color} circle")


# Flyweight Factory Class
class ShapeFactory:
    def __init__(self):
        self._shapes = {}

    def get_shape(self, color):
        # Check if a shape with the color already exists
        if color not in self._shapes:
            self._shapes[color] = Circle(color)
            print(f"Creating new {color} circle")
        return self._shapes[color]


# Client Code
if __name__ == "__main__":
    factory = ShapeFactory()

    # Client requests shapes
    circle1 = factory.get_shape("Red")
    circle1.draw()  # Output: Drawing a Red circle

    circle2 = factory.get_shape("Blue")
    circle2.draw()  # Output: Drawing a Blue circle

    # Reuse the "Red" circle object
    circle3 = factory.get_shape("Red")
    circle3.draw()  # Output: Drawing a Red circle

    # Output shows that only one "Red" circle was created and reused
