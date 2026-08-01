from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} made using Credit Card.")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} made using Debit Card.")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} made using UPI.")


class NetBankingPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} made using Net Banking.")


class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy:
            self.strategy.pay(amount)
        else:
            print("No payment method selected.")


processor = PaymentProcessor()

while True:
    print("\n===== Payment Menu =====")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you! Exiting...")
        break

    amount = float(input("Enter payment amount: $"))

    if choice == "1":
        processor.set_strategy(CreditCardPayment())
    elif choice == "2":
        processor.set_strategy(DebitCardPayment())
    elif choice == "3":
        processor.set_strategy(UPIPayment())
    elif choice == "4":
        processor.set_strategy(NetBankingPayment())
    else:
        print("Invalid choice!")
        continue

    processor.process_payment(amount)
