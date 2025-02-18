# Mediator Interface
class ChatMediator:
    def send_message(self, message, user):
        pass

# Concrete Mediator
class ChatRoom(ChatMediator):
    def __init__(self):
        self.participants = []

    def add_user(self, user):
        self.participants.append(user)
    
    def send_message(self, message, user):
        for participant in self.participants:
            if participant != user:
                participant.receive(message, user)

# Colleague (User)
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.mediator.add_user(self)

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message, sender):
        print(f"{self.name} received from {sender.name}: {message}")

# Client Code
chat_room = ChatRoom()

alice = User("Alice", chat_room)
bob = User("Bob", chat_room)
charlie = User("Charlie", chat_room)

alice.send("Hello, everyone!")
bob.send("Hey Alice!")
charlie.send("Hi all!")
