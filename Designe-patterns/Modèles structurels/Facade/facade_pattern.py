class SubsystemA:
    def operation_a(self):
        return "SubsystemA: Operation A"

class SubsystemB:
    def operation_b(self):
        return "SubsystemB: Operation B"

class SubsystemC:
    def operation_c(self):
        return "SubsystemC: Operation C"

# Facade Class
class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()
    
    def operation(self):
        results = [
            self._subsystem_a.operation_a(),
            self._subsystem_b.operation_b(),
            self._subsystem_c.operation_c()
        ]
        return "Facade: Simplified Interface -> " + ", ".join(results)

# Client Code
def client_code(facade: Facade):
    print(facade.operation())

# Running the code
facade = Facade()
print("Client: Using the Facade:")
client_code(facade)
