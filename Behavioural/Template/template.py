# Abstract Class
from abc import ABC, abstractmethod


class Beverage(ABC):

    # Template Method
    def prepare_recipe(self):
        self.boil_water()
        self.brew()  # This will be implemented by subclasses
        self.pour_in_cup()
        self.add_condiments()  # This will be implemented by subclasses

    # Common Steps (Implemented in Abstract Class)
    def boil_water(self):
        print("Boiling water.")

    def pour_in_cup(self):
        print("Pouring into cup.")

    # Abstract Steps (To be implemented by subclasses)
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


# Concrete Class: Tea
class Tea(Beverage):
    def brew(self):
        print("Steeping the tea.")

    def add_condiments(self):
        print("Adding lemon.")


# Concrete Class: Coffee
class Coffee(Beverage):
    def brew(self):
        print("Dripping coffee through filter.")

    def add_condiments(self):
        print("Adding sugar and milk.")


# Client Code
if __name__ == "__main__":
    tea = Tea()
    tea.prepare_recipe()
    print()
    coffee = Coffee()
    coffee.prepare_recipe()
