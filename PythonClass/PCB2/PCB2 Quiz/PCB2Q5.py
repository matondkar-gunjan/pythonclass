def calculate_grocery_total():
      total = 0
      items = ["Apples", "Bread", "Milk", "Eggs"]
      prices = [3.50, 2.00, 4.00, 1.50]
      for x in prices:
            total += x
      print("The total cost of your grocery shopping is: ", total)
calculate_grocery_total()
