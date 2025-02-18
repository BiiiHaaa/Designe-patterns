from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"💳 Paid ${amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"📧 Paid ${amount} using PayPal.")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"₿ Paid ${amount} using Bitcoin.")

# Context (Payment Processor)
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def checkout(self, amount):
        self.strategy.pay(amount)

# Client Code
payment = PaymentProcessor(CreditCardPayment())  # Default strategy: Credit Card
payment.checkout(100)

payment.set_strategy(PayPalPayment())  # Change to PayPal
payment.checkout(200)

payment.set_strategy(BitcoinPayment())  # Change to Bitcoin
payment.checkout(300)
