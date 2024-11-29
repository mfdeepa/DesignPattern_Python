# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal.")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Bitcoin.")


# Context
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)


# Client Code
if __name__ == "__main__":
    payment_context = PaymentContext(CreditCardPayment())  # Default strategy is CreditCardPayment
    payment_context.execute_payment(100)  # Paying 100 using Credit Card.

    # Switch strategy at runtime
    payment_context.set_strategy(PayPalPayment())
    payment_context.execute_payment(200)  # Paying 200 using PayPal.

    payment_context.set_strategy(BitcoinPayment())
    payment_context.execute_payment(300)  # Paying 300 using Bitcoin.
