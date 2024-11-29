from Creational.Builder.builder.ConputerBuilder import ComputerBuilder
from Creational.Builder.builder.computerDirector import ComputerDirector

if __name__ == "__main__":
    builder = ComputerBuilder()
    director = ComputerDirector(builder)
    computer = director.construct()
    print(computer)