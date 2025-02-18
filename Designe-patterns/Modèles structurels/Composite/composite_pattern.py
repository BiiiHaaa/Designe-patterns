from abc import ABC, abstractmethod

# Component Interface
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Leaf Class
class Leaf(Component):
    def __init__(self, name):
        self.name = name
    
    def operation(self):
        return f"Leaf: {self.name}"

# Composite Class
class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component: Component):
        self.children.append(component)
    
    def remove(self, component: Component):
        self.children.remove(component)
    
    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Composite: {self.name} [{', '.join(results)}]"

# Client Code
def client_code(component: Component):
    print(component.operation())

# Running the code
leaf1 = Leaf("Leaf 1")
leaf2 = Leaf("Leaf 2")
composite = Composite("Composite 1")
composite.add(leaf1)
composite.add(leaf2)

print("Single Leaf Object:")
client_code(leaf1)

print("\nComposite Object with Leaves:")
client_code(composite)
