def get_price_per_scoop():
      return 2.50

def get_serving_price(serving_choice):
      serving_prices = {
            "cup" : 0,
            "biscuit cone" : 1.00,
            "waffle cone" : 1.50,
            "milkshake" : 2.00
}
      return serving_prices.get(serving_choice, 0)

def calculate_total_cost(scoops, serving_choice):
      price_per_scoop = get_price_per_scoop()
      serving_price = get_serving_price(serving_choice)
      total = (scoops * price_per_scoop) + serving_price
      return total

if __name__ == "__main__":
      price_per_scoop = get_price_per_scoop()
      print(f"Price per scoop: ${get_price_per_scoop()}")
      print(f"Price for 'cup': ${get_serving_price('cup')}")
      print(f"3 scoops in a cup: ${calculate_total_cost(3, 'cup')}")
