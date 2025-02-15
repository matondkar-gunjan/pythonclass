class BankAccount:
      def __init__(self, accountNumber, name, balance):
            self.accountNumber = accountNumber
            self.name = name
            self.balance = balance
            
      def Deposit(self, deposit_amount):
            self.balance = self.balance + deposit_amount
            
      def Withdrawal(self, withdrawal_amount):
            if withdrawal_amount > self.balance:
                  print("Impossible operation! Insufficient balance !")
            else:
                  self.balance - withdrawal_amount
                  
      def bankFees(self):
            self.balance = self.balance * 0.92
            
      def display(self):
            print("Account Number : ", self.accountNumber)
            print("Accout Name : ", self.name)
            print("Account Balance : $", self.balance)

myBank = BankAccount(82821908218921892172980, "Gunjan", 1000)

myBank.Withdrawal(300)
myBank.Deposit(200)
myBank.display()
