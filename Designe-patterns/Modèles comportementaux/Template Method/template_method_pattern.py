from abc import ABC, abstractmethod

# Abstract Class (Template)
class Beverage(ABC):
    def prepare(self):
        """ Template method defining the steps for preparing a beverage """
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water...")

    def pour_in_cup(self):
        print("Pouring into cup...")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

# Concrete Class for Tea
class Tea(Beverage):
    def brew(self):
        print("Steeping the tea...")

    def add_condiments(self):
        print("Adding lemon...")

# Concrete Class for Coffee
class Coffee(Beverage):
    def brew(self):
        print("Dripping coffee through filter...")

    def add_condiments(self):
        print("Adding sugar and milk...")

# Client Code
print("Preparing Tea:")
tea = Tea()
tea.prepare()

print("\nPreparing Coffee:")
coffee = Coffee()
coffee.prepare()
