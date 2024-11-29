# Subject
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

# Observer Interface
class Observer:
    def update(self, temperature):
        pass

# Concrete Observer
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"Phone Display: Temperature updated to {temperature}°C")

class WindowDisplay(Observer):
    def update(self, temperature):
        print(f"Window Display: Temperature updated to {temperature}°C")

# Usage
if __name__ == "__main__":
    station = WeatherStation()
    phone = PhoneDisplay()
    window = WindowDisplay()

    station.add_observer(phone)
    station.add_observer(window)

    station.set_temperature(25)  # Updates both displays
    station.remove_observer(phone)
    station.set_temperature(30)  # Updates only the window display
