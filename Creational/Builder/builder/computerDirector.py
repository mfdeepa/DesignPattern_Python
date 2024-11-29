class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        #  set values as per user

        self.builder.set_cpu(2)
        self.builder.set_ram(2)
        self.builder.set_storage(2)
        self.builder.set_power_supply(5)
        return self.builder.build()



