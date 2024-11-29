from abc import ABC, abstractmethod


# Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass


# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Base cost of a simple coffee


# Decorator Base Class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass


# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Adding cost for milk


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Adding cost for sugar


class WhipDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3  # Adding cost for whipped cream


# Client Code
if __name__ == "__main__":
    # Order a simple coffee
    simple_coffee = SimpleCoffee()
    print(f"Simple Coffee cost: ${simple_coffee.cost()}")

    # Order a coffee with milk
    milk_coffee = MilkDecorator(simple_coffee)
    print(f"Coffee with milk cost: ${milk_coffee.cost()}")

    # Order a coffee with milk and sugar
    milk_sugar_coffee = SugarDecorator(milk_coffee)
    print(f"Coffee with milk and sugar cost: ${milk_sugar_coffee.cost()}")

    # Order a coffee with milk, sugar, and whip
    full_coffee = WhipDecorator(milk_sugar_coffee)
    print(f"Coffee with milk, sugar, and whip cost: ${full_coffee.cost()}")
