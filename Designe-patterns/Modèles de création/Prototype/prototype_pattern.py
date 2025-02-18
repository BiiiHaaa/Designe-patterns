import copy

# Prototype Base Class
class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Concrete Prototype
class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value
    
    def display(self):
        print(f"ConcretePrototype with value: {self.value}")

# Client Code
prototype = ConcretePrototype("Original")
prototype.display()

# Cloning the prototype
cloned_prototype = prototype.clone()
cloned_prototype.display()

# Modifying the cloned object
cloned_prototype.value = "Cloned"
cloned_prototype.display()
prototype.display()  # Ensuring the original object is unchanged
