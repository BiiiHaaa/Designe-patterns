from abc import ABC, abstractmethod

# Abstract Product A
class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass

# Abstract Product B
class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass

# Concrete Product A1
class ProductA1(AbstractProductA):
    def operation_a(self):
        return "Product A1 operation"

# Concrete Product A2
class ProductA2(AbstractProductA):
    def operation_a(self):
        return "Product A2 operation"

# Concrete Product B1
class ProductB1(AbstractProductB):
    def operation_b(self):
        return "Product B1 operation"

# Concrete Product B2
class ProductB2(AbstractProductB):
    def operation_b(self):
        return "Product B2 operation"

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Concrete Factory 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ProductB1()

# Concrete Factory 2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA2()
    
    def create_product_b(self) -> AbstractProductB:
        return ProductB2()

# Client Code
def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    print(product_a.operation_a())
    print(product_b.operation_b())

# Running the client with different factories
print("Using ConcreteFactory1:")
client_code(ConcreteFactory1())

print("\nUsing ConcreteFactory2:")
client_code(ConcreteFactory2())
