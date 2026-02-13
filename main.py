class PayPal:
    def pay(self, amount):
        return f"paypal pay {amount}"

class Click:
    def pay(self, amount):
        return f"click pay {amount}"

def checkout(gateway, amount):
    return gateway.pay(amount)

print(checkout(PayPal(), 10))
print(checkout(Click(), 10))
