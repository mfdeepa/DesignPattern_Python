class Computer:
    def __init__(self):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.power_supply = 0
        self.storage = 0

    def __str__(self):
        return (f"cpu = {self.cpu},ram = {self.ram}, gpu = {self.gpu}, power = {self.power_supply}, storage = {self.storage}")