from abc import ABC, abstractmethod

# Product
class Product:
    def __init__(self):
        self.parts = []
    
    def add(self, part):
        self.parts.append(part)
    
    def show(self):
        return "Product Parts: " + ", ".join(self.parts)

# Builder Interface
class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass
    
    @abstractmethod
    def build_part_b(self):
        pass
    
    @abstractmethod
    def get_result(self):
        pass

# Concrete Builder
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()
    
    def build_part_a(self):
        self.product.add("Part A")
    
    def build_part_b(self):
        self.product.add("Part B")
    
    def get_result(self):
        return self.product

# Director
class Director:
    def __init__(self, builder: Builder):
        self.builder = builder
    
    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()

# Client Code
builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.get_result()
print(product.show())
