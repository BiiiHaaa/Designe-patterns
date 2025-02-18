from abc import ABC, abstractmethod

# Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_element_a(self, element):
        pass
    
    @abstractmethod
    def visit_element_b(self, element):
        pass

# Element Interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

# Concrete Element A
class ConcreteElementA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_element_a(self)
    
    def operation_a(self):
        return "Element A operation"

# Concrete Element B
class ConcreteElementB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_element_b(self)
    
    def operation_b(self):
        return "Element B operation"

# Concrete Visitor
class ConcreteVisitor(Visitor):
    def visit_element_a(self, element: ConcreteElementA):
        print(f"Visiting {element.operation_a()}")
    
    def visit_element_b(self, element: ConcreteElementB):
        print(f"Visiting {element.operation_b()}")

# Client Code
elements = [ConcreteElementA(), ConcreteElementB()]
visitor = ConcreteVisitor()

for element in elements:
    element.accept(visitor)
