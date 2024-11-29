class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = "Singleton Instance"


# Usage
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # Output: True
