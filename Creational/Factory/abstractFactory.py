from abc import ABC, abstractmethod


# Abstract Product Interfaces
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


# Concrete Products
class WindowsButton(Button):
    def render(self):
        return "Rendering Windows Button"


class MacOSButton(Button):
    def render(self):
        return "Rendering MacOS Button"


class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering Windows Checkbox"


class MacOSCheckbox(Checkbox):
    def render(self):
        return "Rendering MacOS Checkbox"


# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


# Client Code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())


if __name__ == "__main__":
    # Using Windows Factory
    print("Windows GUI:")
    client_code(WindowsFactory())

    # Using MacOS Factory
    print("\nMacOS GUI:")
    client_code(MacOSFactory())
