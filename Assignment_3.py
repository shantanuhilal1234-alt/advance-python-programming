from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    
    def set_strategy(self, strategy):
        self.strategy = strategy

   
     def process_payment(self, amount):
        self.strategy.pay(amount)

processor = PaymentProcessor(CreditCardPayment())

print("Payment Method: Credit Card")
processor.process_payment(2500)

print("\nChanging Payment Method to UPI")
processor.set_strategy(UPIPayment())
processor.process_payment(1800)

print("\nChanging Payment Method to PayPal")
processor.set_strategy(PayPalPayment())
processor.process_payment(3200)
