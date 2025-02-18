from abc import ABC, abstractmethod

# Implementor Interface
class Implementor(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass

# Concrete Implementations
class ConcreteImplementorA(Implementor):
    def operation_implementation(self):
        return "ConcreteImplementorA: Operation implementation."

class ConcreteImplementorB(Implementor):
    def operation_implementation(self):
        return "ConcreteImplementorB: Operation implementation."

# Abstraction
class Abstraction:
    def __init__(self, implementor: Implementor):
        self.implementor = implementor
    
    def operation(self):
        return f"Abstraction: Delegating to {self.implementor.operation_implementation()}"

# Refined Abstraction
class RefinedAbstraction(Abstraction):
    def operation(self):
        return f"RefinedAbstraction: Extended {self.implementor.operation_implementation()}"

# Client Code
def client_code(abstraction: Abstraction):
    print(abstraction.operation())

# Running the code
implementor_a = ConcreteImplementorA()
implementor_b = ConcreteImplementorB()

abstraction1 = Abstraction(implementor_a)
abstraction2 = RefinedAbstraction(implementor_b)

print("Using Abstraction with ConcreteImplementorA:")
client_code(abstraction1)

print("\nUsing RefinedAbstraction with ConcreteImplementorB:")
client_code(abstraction2)
