from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command: Turn On Command
class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()

# Concrete Command: Turn Off Command
class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()

# Receiver: Light
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

# Invoker: RemoteControl
class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command: Command):
        self._command = command

    def press_button(self):
        self._command.execute()

# Client Code
if __name__ == "__main__":
    # Create receiver (light)
    light = Light()

    # Create command objects
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Create invoker (remote control)
    remote = RemoteControl()

    # Turn light on using the remote
    remote.set_command(light_on)
    remote.press_button()  # Output: Light is ON

    # Turn light off using the remote
    remote.set_command(light_off)
    remote.press_button()  # Output: Light is OFF
