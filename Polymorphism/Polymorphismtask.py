class Payment:
    def pay(self):
        print("Processing payment...")

# Child Class 1
class GooglePay(Payment):
    def pay(self):  # Method Overriding
        print("Payment done using Google Pay ")

# Child Class 2
class PhonePe(Payment):
    def pay(self):  # Method Overriding
        print("Payment done using PhonePe ")

# Child Class 3
class CreditCard(Payment):
    def pay(self):  # Method Overriding
        print("Payment done using Credit Card ")


# Creating Objects
p1 = Payment()
p2 = GooglePay()
p3 = PhonePe()
p4 = CreditCard()

# Calling pay() Method
p1.pay()
p2.pay()
p3.pay()
p4.pay()
