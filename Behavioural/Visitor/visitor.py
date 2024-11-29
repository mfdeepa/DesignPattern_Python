from abc import ABC, abstractmethod


# Visitor Interface
class ShoppingCartVisitor(ABC):

    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_electronics(self, electronics):
        pass


# Concrete Visitor
class ShoppingCart(ShoppingCartVisitor):

    def visit_book(self, book):
        print(f"Calculating price for book: {book.name}")
        return book.price * 0.9  # 10% discount

    def visit_electronics(self, electronics):
        print(f"Calculating price for electronics: {electronics.name}")
        return electronics.price * 1.1  # 10% tax added


# Element Interface
class Item(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


# Concrete Elements
class Book(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        return visitor.visit_book(self)


class Electronics(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        return visitor.visit_electronics(self)


# Object Structure (Shopping Cart)
class ShoppingCartItems:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self, visitor):
        total = 0
        for item in self.items:
            total += item.accept(visitor)
        return total


# Client Code
if __name__ == "__main__":
    book1 = Book("Design Patterns",  30)
    book2 = Book("Clean Code", 25)
    electronics1 = Electronics("Smartphone", 200)

    cart = ShoppingCartItems()
    cart.add_item(book1)
    cart.add_item(book2)
    cart.add_item(electronics1)

    visitor = ShoppingCart()
    print(visitor.visit_book(book1))
    print(visitor.visit_electronics(electronics1))
    total = cart.calculate_total(visitor)
    print(f"Total cost: {total}")
