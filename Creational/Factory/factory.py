from abc import ABC, abstractmethod


# Product Interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


# Concrete Products
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"


class Square(Shape):
    def draw(self):
        return "Drawing a Square"


# Factory Class
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "SQUARE":
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")


# Client Code
if __name__ == "__main__":
    shape = ShapeFactory.get_shape("CIRCLE")
    print(shape.draw())  # Output: Drawing a Circle

    shape = ShapeFactory.get_shape("SQUARE")
    print(shape.draw())  # Output: Drawing a Square
