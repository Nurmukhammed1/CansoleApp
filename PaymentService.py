from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def collectPaymentDetails(self):
        pass

    @abstractmethod
    def validatePaymentDetails(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentStrategy):

    def __init__(self, cardNumber, expiracyDate, cvv):
        self.__cardNumber = cardNumber
        self.__expiracyDate = expiracyDate
        self.__cvv = cvv

    def collectPaymentDetails(self):
        print("Collecting Credit Card Details...")

    def validatePaymentDetails(self):
        print(f"Validating Credit Card info {self.__cardNumber}")

    def pay(self, amount):
        print(f"Paying {amount}$ using Credit Card \n"
              f"Payment approved")

class PayPal(PaymentStrategy):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def collectPaymentDetails(self):
        print("Collecting PayPal Details...")

    def validatePaymentDetails(self):
        print("Validating")

    def pay(self, amount):
        print(f"Paying {amount}$ using PayPal \n"
              f"Payment approved")

class DebitCard(PaymentStrategy):

    def __init__(self, cardNumber, expiracyDate, cvv):
        self.__cardNumber = cardNumber
        self.__expiracyDate = expiracyDate
        self.__cvv = cvv

    def collectPaymentDetails(self):
        print("Collecting Debit Card Details...")

    def validatePaymentDetails(self):
        print(f"Validating Debit Card info {self.__cardNumber}")

    def pay(self, amount):
        print(f"Paying {amount}$ using Debit Card \n"
              f"Payment approved")

class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def perform_payment(self, amount):
        self.payment_strategy.collectPaymentDetails()
        self.payment_strategy.validatePaymentDetails()
        self.payment_strategy.pay(amount)
