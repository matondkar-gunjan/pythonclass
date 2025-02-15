def display_flavors():
      flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookies and cream"]
      print("Available Ice Cream Flavors:")
      index = 1
      for flavor in flavors:
            print(f"{index}.{flavor}")
            index += 1

      return flavors

def display_serving_options():
      print("\n")
      options = ["Cup", "Biscuit cone", "Waffle cone", "Milkshake"]
      print("Available Serving Options:")
      index = 1
      for option in options:
            print(f"{index}.{option}")
            index += 1

      return options

def is_valid_choice(choice, options):
      if choice >= 1 and choice <= len(options):
            return True
      else:
            return False

if __name__ == "__main__":
      flavors = display_flavors()
      options = display_serving_options()
      print(f"Is choice 2 valid? {is_valid_choice(2, options)}")
      print(f"Is option 2 valid? {is_valid_choice(5, options)}")
