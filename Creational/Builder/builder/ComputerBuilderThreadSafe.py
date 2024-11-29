# If the Builder or Product is shared across threads, you must ensure thread safety

from threading import Lock

from Creational.Builder.builder.Computer import Computer


class ComputerBuilderThreadSafe:
    def __init__(self):
        self.lock = Lock()
        self.computer = Computer()

    def set_cpu(self, cpu):
        with self.lock:
            self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        with self.lock:
            self.computer.ram = ram
        return self

    def set_storage(self, storage):
        with self.lock:
            self.computer.storage = storage
        return self

    def build(self):
        with self.lock:
            return self.computer
