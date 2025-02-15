from Inventory import display_flavors, display_serving_options, is_valid_choice
from Pricing import calculate_total_cost

def take_order():
      print("Welcome to the Ice cream Shop!")
      flavors = display_flavors()
      flavor_choice = int(input("Please choose a flavor by entering the number: "))

      if is_valid_choice(flavor_choice, flavors):
            scoops = int(input("How many scoops would you like?: "))
            if scoops < 1:
                  print("You need at least one scoop")
                  return 0

            serving_options = display_serving_options()
            serving_choice_num = int(input("Please choose a serving option by entering the number: "))
            if is_valid_choice(serving_choice_num, serving_options):
                  serving_choice = serving_options[serving_choice_num - 1].lower() 
                  total_cost = calculate_total_cost(scoops, serving_choice)
                  print(f"Your total for {scoops} scoops in a {serving_choice} is: ${total_cost}")
            else:
                  print("Invalid choice! Please select a valid serving option.")
      else:
            print("Invalid choice! Please select a valid flavor.")
      
