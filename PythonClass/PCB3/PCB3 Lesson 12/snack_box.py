from vending_machine import VendingMachine

class SnackBox:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def dispense(self, user_balance):
        """
        Deducts the snack's cost from the user's balance and updates the transaction log.
        :param user_balance: int, the user's current balance in coins
        :return: int, the updated user balance
        """
        if user_balance >= self.cost:
            user_balance -= self.cost
            VendingMachine.transaction_log.append(self.name)
            print(f"{self.name} has been dispensed.")
        else:
            print("There are insufficient funds.")
        return user_balance

class PartyPack(SnackBox):
    def __init__(self):
        super().__init__("Party Pack", 30)

class DeluxeBox(SnackBox):
    def __init__(self):
        super().__init__("Deluxe Box", 70)
