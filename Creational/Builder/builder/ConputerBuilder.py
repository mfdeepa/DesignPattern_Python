from Creational.Builder.builder.ComputerAbstract import ComputerAbstract
from Computer import Computer


class ComputerBuilder(ComputerAbstract):

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        if cpu < 2:
            raise ValueError("CPU must be at least 2")
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_power_supply(self, power):
        self.computer.power = power
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer
