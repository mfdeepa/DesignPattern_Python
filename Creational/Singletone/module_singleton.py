class Singleton:
    def __init__(self):
        self.value = "Singleton Instance"


singleton_instance = Singleton()

if __name__ == "__main__":
    s1 = singleton_instance
    s2 = singleton_instance
    print(s1 is s2)  # Output: True
