# Mediator Interface
class Mediator:
    def notify(self, sender, event):
        pass

# Concrete Mediator
class ChatRoom(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        user.mediator = self

    def notify(self, sender, message):
        for user in self.users:
            if user != sender:
                user.receive(message)

# Colleague
class User:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.notify(self, message)

    def receive(self, message):
        print(f"{self.name} receives: {message}")


# Client Code
if __name__ == '__main__':
    chat = ChatRoom()
    alice = User("Alice")
    bob = User("Bob")

    chat.add_user(alice)
    chat.add_user(bob)

    alice.send("Hello!")
    bob.send("Hi!")
