class Target:
    """The Target defines the domain-specific interface used by the client."""
    def request(self):
        return "Target: Default behavior"

class Adaptee:
    """The Adaptee contains some useful behavior, but its interface is incompatible
    with the client. The Adaptee needs some adaptation before the client can use it.
    """
    def specific_request(self):
        return "Adaptee: Specific behavior"

class Adapter(Target):
    """The Adapter makes the Adaptee's interface compatible with the Target's
    interface."""
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (Translated) {self.adaptee.specific_request()}"

# Client Code
def client_code(target: Target):
    print(target.request())

print("Client: I can work with the Target objects:")
target = Target()
client_code(target)

print("\nClient: The Adaptee class has a different interface. See:")
adaptee = Adaptee()
print(adaptee.specific_request())

print("\nClient: But I can work with it using an Adapter:")
adapter = Adapter(adaptee)
client_code(adapter)
