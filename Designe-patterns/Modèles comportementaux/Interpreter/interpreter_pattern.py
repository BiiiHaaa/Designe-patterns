from abc import ABC, abstractmethod

# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

# Terminal Expression (for numbers)
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

# Non-Terminal Expression (for operations)
class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

# Client Code - Parsing and Evaluating an Expression
def parse_expression(expression):
    tokens = expression.split()
    stack = []
    
    for token in tokens:
        if token.isdigit():
            stack.append(Number(int(token)))
        elif token == '+':
            right = stack.pop()
            left = stack.pop()
            stack.append(Add(left, right))
        elif token == '-':
            right = stack.pop()
            left = stack.pop()
            stack.append(Subtract(left, right))
    
    return stack.pop().interpret()

# Example Usage
expression = "5 10 + 3 -"  # Equivalent to (5 + 10) - 3
result = parse_expression(expression)
print(f"Result: {result}")  # Output: Result: 12
