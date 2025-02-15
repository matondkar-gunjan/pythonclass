class VendingMachine:
    # Class attribute to store the transaction log
    transaction_log = []

    @staticmethod
    def view_stats(user_balance):
        """
        Display the user's balance and the contents of the transaction log.
        :param user_balance: int, the user's balance in coins
        """
        print(f"User balance: {user_balance} coins")

        # Create a shallow copy of the transaction log
        log_snapshot = VendingMachine.transaction_log[:]

        if log_snapshot:
            print("Transaction log contents:")
            for item in log_snapshot:
                print(f"- {item}")
        else:
            print("Nothing is inside at the moment")

    @staticmethod
    def sell_items(user_balance):
        """
        Simulates selling the items in the transaction log for coins.
        :param user_balance: int, the user's balance in coins
        :return: int, the updated user balance
        """
        if VendingMachine.transaction_log:
            # Calculate earnings based on the number of items in the log
            earnings = len(VendingMachine.transaction_log) * 20  # Assuming each item earns 10 coins
            user_balance += earnings

            print(f"Sold {len(VendingMachine.transaction_log)} items for {earnings} coins.")

            # Clear the transaction log
            VendingMachine.transaction_log = []
            print("Your transaction log is now empty.")
        else:
            print("No items are available to sell.")

        return user_balance
