import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()  # Lock object for thread safety

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # First check (no locking for performance)
            with cls._lock:  # Acquire lock
                if not cls._instance:  # Second check (after acquiring lock)
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# Usage
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(singleton1 is singleton2)  # Output: True (both are same instance)
