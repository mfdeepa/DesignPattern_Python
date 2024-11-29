# State Interface
class State:
    def insert_coin(self):
        pass

    def press_button(self):
        pass

    def dispense(self):
        pass

# Concrete States
class NoCoinState(State):
    def insert_coin(self):
        print("Coin inserted.")
        return HasCoinState()

class HasCoinState(State):
    def press_button(self):
        print("Button pressed. Dispensing item.")
        return DispensedState()

class DispensedState(State):
    def dispense(self):
        print("Item dispensed. Returning to no coin state.")
        return NoCoinState()

# Context
class VendingMachine:
    def __init__(self):
        self.state = NoCoinState()

    def insert_coin(self):
        self.state = self.state.insert_coin()

    def press_button(self):
        self.state = self.state.press_button()

    def dispense(self):
        self.state = self.state.dispense()

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.insert_coin()
    vending_machine.press_button()
    vending_machine.dispense()
