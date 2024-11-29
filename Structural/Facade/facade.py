# Subsystem Classes
class Light:
    def turn_on(self):
        return "Lights are turned ON"

    def turn_off(self):
        return "Lights are turned OFF"


class AirConditioner:
    def turn_on(self):
        return "Air Conditioner is turned ON"

    def turn_off(self):
        return "Air Conditioner is turned OFF"


class Television:
    def turn_on(self):
        return "Television is turned ON"

    def turn_off(self):
        return "Television is turned OFF"


# Facade Class
class HomeAutomationFacade:
    def __init__(self):
        self.light = Light()
        self.air_conditioner = AirConditioner()
        self.television = Television()

    def turn_on_all(self):
        return "\n".join([
            self.light.turn_on(),
            self.air_conditioner.turn_on(),
            self.television.turn_on()
        ])

    def turn_off_all(self):
        return "\n".join([
            self.light.turn_off(),
            self.air_conditioner.turn_off(),
            self.television.turn_off()
        ])


# Client Code
if __name__ == "__main__":
    # Using the Facade
    home = HomeAutomationFacade()
    print("Turning ON all devices:")
    print(home.turn_on_all())

    print("\nTurning OFF all devices:")
    print(home.turn_off_all())
