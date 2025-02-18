import weakref

class Flyweight:
    """The Flyweight stores shared state (intrinsic state) that belongs to multiple real objects."""
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        return f"Flyweight: Shared ({self.shared_state}) - Unique ({unique_state})"

class FlyweightFactory:
    """Manages Flyweight instances and ensures that they are shared properly."""
    _flyweights = weakref.WeakValueDictionary()
    
    @staticmethod
    def get_flyweight(shared_state):
        if shared_state not in FlyweightFactory._flyweights:
            FlyweightFactory._flyweights[shared_state] = Flyweight(shared_state)
        return FlyweightFactory._flyweights[shared_state]

# Client Code
def client_code(shared, unique):
    flyweight = FlyweightFactory.get_flyweight(shared)
    print(flyweight.operation(unique))

# Running the code
print("Using Flyweight pattern:")
client_code("State1", "UniqueA")
client_code("State1", "UniqueB")
client_code("State2", "UniqueC")
