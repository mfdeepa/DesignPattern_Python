from abc import ABC, abstractmethod


# Subject Interface
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


# RealSubject: The actual object being proxied
class RealSubject(Subject):
    def __init__(self):
        print("Initializing RealSubject...")

    def request(self):
        print("Request made to RealSubject")


# Proxy: Controls access to RealSubject
class Proxy(Subject):
    def __init__(self):
        self._real_subject = None

    def request(self):
        # Lazy initialization
        if self._real_subject is None:
            self._real_subject = RealSubject()
        self._real_subject.request()


# Client Code
if __name__ == "__main__":
    # Create a proxy object
    proxy = Proxy()

    # Make a request. The RealSubject is initialized only at this point.
    proxy.request()  # Output: Initializing RealSubject... / Request made to RealSubject
    proxy.request()  # Output: Request made to RealSubject (No re-initialization)
