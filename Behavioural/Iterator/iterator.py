# Iterator Interface
from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


# Concrete Iterator
class BookIterator(Iterator):
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __next__(self):
        if not self.has_next():
            raise StopIteration
        book = self.books[self.index]
        self.index += 1
        return book

    def has_next(self):
        return self.index < len(self.books)


# Aggregate (Collection)
class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def create_iterator(self):
        return BookIterator(self.books)


# Client Code

if __name__ == "__main__":
    collection = BookCollection()
    collection.add_book("The Great Gatsby")
    collection.add_book("1984")
    collection.add_book("To Kill a Mockingbird")

    iterator = collection.create_iterator()

    while iterator.has_next():
        print(iterator.__next__())
