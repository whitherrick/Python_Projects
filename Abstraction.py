from abc import ABC, abstractmethod

class Diner(ABC):
    def TotalCost(self, amount):
        print("Your total is: ", amount)

    @abstractmethod
    def payment(self, amount):
        pass

class CreditPayment(Diner):
    def payment(self, amount):
        print("Your total for the meal is {}. Thank you for your visit!".format(amount))

obj = CreditPayment()
obj.TotalCost("$50")
obj.payment("$50")
