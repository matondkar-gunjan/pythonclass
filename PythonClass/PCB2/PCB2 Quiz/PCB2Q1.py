orig_balance= 1000
print("You have", orig_balance, "dollars")
while orig_balance != 0:
      withdrawn = int(input("Enter amount to withdraw: "))
      if withdrawn <= orig_balance:
            orig_balance = orig_balance - withdrawn   
            print("Amount of money left: ", orig_balance)
      else:
            print("Insufficiennt funds")
            
