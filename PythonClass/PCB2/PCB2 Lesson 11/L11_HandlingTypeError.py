item_prices = [10.99, 5.49, 3, 8.99]
try:
      total_price = sum(item_prices)
      print("The total price of items in the cart is", total_price)
except TypeError:
      print("Oops! All items prices should be numbers")
