# main.py

from vending_machine import VendingMachine
from snack_box import PartyPack, DeluxeBox

def main():
    user_balance = 100
    while True:
        print(f"\n=== Current Balance: {user_balance} coins ===")
        print("\n=== Vending Machine Menu ===")
        print("1. Buy Party Pack (30 coins)")
        print("2. Buy Deluxe Box (70 coins)")
        print("3. View Stats")
        print("4. Sell Items (Earn 20 coins per item)")
        print("5. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            user_balance = PartyPack().dispense(user_balance)
        elif choice == "2":
            user_balance = DeluxeBox().dispense(user_balance)
        elif choice == "3":
            VendingMachine.view_stats(user_balance)
        elif choice == "4":
            user_balance = VendingMachine.sell_items(user_balance)
        elif choice == "5":
            print("Exiting the vending machine. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
