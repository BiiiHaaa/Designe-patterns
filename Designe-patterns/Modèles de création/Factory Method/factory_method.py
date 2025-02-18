from abc import ABC, abstractmethod

# Product Interface
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Product A
class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation"

# Concrete Product B
class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation"

# Creator (Factory) Interface
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass
    
    def some_operation(self):
        product = self.factory_method()
        return f"Creator: Working with {product.operation()}"

# Concrete Creator A
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

# Concrete Creator B
class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Client Code
def client_code(creator: Creator):
    print(creator.some_operation())

print("Using ConcreteCreatorA:")
client_code(ConcreteCreatorA())

print("\nUsing ConcreteCreatorB:")
client_code(ConcreteCreatorB())
