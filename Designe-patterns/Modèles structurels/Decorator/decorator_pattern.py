from abc import ABC, abstractmethod

# Component Interface
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Component
class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent: Base operation"

# Decorator Base Class
class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component
    
    def operation(self):
        return self._component.operation()

# Concrete Decorators
class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA: {super().operation()}"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB: {super().operation()}"

# Client Code
def client_code(component: Component):
    print(component.operation())

# Running the code
simple = ConcreteComponent()
print("Client: Basic Component:")
client_code(simple)

# Applying decorators
decorator1 = ConcreteDecoratorA(simple)
decorator2 = ConcreteDecoratorB(decorator1)

print("\nClient: Decorated Component:")
client_code(decorator2)
