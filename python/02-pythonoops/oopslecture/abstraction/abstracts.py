from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass  # Enforces that all child classes MUST write this method


class StripePayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe API."


# p = PaymentProcessor()  # Error! Cannot instantiate abstract class
stripe = StripePayment()
print(stripe.process_payment(100))
