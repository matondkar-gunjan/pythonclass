import random

class BaseMilkTea:
      def __init__(self):
            self.ingredients = ["tea", "sugar", "milk powder"]

      def drink_name(self):
            pass #This will be overidden in subclasses

class IcedMilkTea(BaseMilkTea):
      def __init__(self):
            super().__init__()
            self.ingredients.extend(["pearls"])

      def drink_name(self):
            return "Iced Original Milk Tea"

class ChocolateMilkTea(BaseMilkTea):
      def __init__(self):
            super().__init__()
            self.ingredients.extend(["chocolate", "fresh milk"])

      def drink_name(self):
            return "Chocolate Milk Tea"

class TaroMilkTea(BaseMilkTea):
      def __init__(self):
            super().__init__()
            self.ingredients.extend(["taro", "syrup", "fresh milk"])

      def drink_name(self):
            return "Taro Milk Tea"

class BubbleTeaStore:
      def __init__(self):
            self.menu = {
                  "Iced Milk Tea" : IcedMilkTea(),
                  "Chocolate Milk Tea" : ChocolateMilkTea(),
                  "Taro Milk Tea" : TaroMilkTea()
                  }

            self.all_ingredients = ["milk powder", "sugar", "tea", "pearls", "chocolate", "fresh milk", "taro", "syrup"]

      def show_menu(self):
            print("Welcome to the Bubble Tea Store! Here is our menu:")
            for drink in self.menu:
                  print(drink)
            print("\n")
            print("Available ingredients in the store:")

            index = 1
            for ingredients in self.all_ingredients:
                  print(f"{index}.{ingredients}")
                  index += 1

      def randomly_order_drink(self):
            drink_name = random.choice(list(self.menu.keys()))
            drink = self.menu[drink_name]
            print("\n")
            print(f"You randomly ordered: {drink.drink_name()}")
            return drink
      

      def play_game(self, drink):
            print("\n")
            print(f"Can you guess the ingredients of {drink.drink_name()}?")
            correct_guesses = []
            ingredients_remaining = len(drink.ingredients)
            while ingredients_remaining > 0:
                  print(f"Ingredients left to guess: {ingredients_remaining}")
                  user_guess = input("Enter an ingredient: ").lower()
                  if user_guess in drink.ingredients and user_guess not in correct_guesses:
                        correct_guesses.append(user_guess)
                        ingredients_remaining -= 1
                        print("Correct!\n")
                  else:
                        print("Incorrect or already guessed! \n")
            print("\n")
            print("\n")
            print(f"Absolutely right! All ingredients for {drink.drink_name()} are: ")

            count = 1
            for ingredient in drink.ingredients:
                  print(f"{count}.{ingredient}")
                  count += 1


def main():
      store = BubbleTeaStore()
      store.show_menu()
      print("\n")
      num_customers = int(input("How many customers are there? "))

      for i in range(num_customers):
            print("\n")
            print(f"Customer{i+1}, it's your turn!")
            drink = store.randomly_order_drink()
            store.play_game(drink)

      print("\n")
      print("All orders are completed. Thank you for playing!")

main()
