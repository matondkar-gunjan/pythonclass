class Farm:
      #Class attributes
      money = 50
      def __init__(self, crop_type, growing_time, yield_amount, cost):
            self.crop_type = crop_type
            self.growing_time = growing_time
            self.yield_amount = yield_amount
            self.cost = cost

      def plant_seed(self):
            Farm.money -= self.cost
      
      @staticmethod
      def view_stats(wheat_yield, tomato_yield, carrot_yield):
            print("\n=== Current Stats ===")
            print(f"Money: {Farm.money} coins")
            print(f"Wheat Yield: {wheat_yield} units")
            print(f"Tomato Yield: {tomato_yield} units")
            print(f"Carrot Yield: {carrot_yield} units")

class Wheat(Farm):
      def __init__(self, crop_type = "Wheat", growing_time = 2, yield_amount = 3, cost = 10):
            super().__init__(crop_type, growing_time, yield_amount, cost)

class Tomato(Farm):
      def __init__(self, crop_type = "Tomato", growing_time = 3, yield_amount = 2, cost = 15):
            super().__init__(crop_type, growing_time, yield_amount, cost)
            
class Carrot(Farm):
      def __init__(self, crop_type = "Carrot", growing_time = 3, yield_amount = 2, cost = 12 ):
            super().__init__(crop_type, growing_time, yield_amount, cost)
            
def main():
      #Main function to run the Farming Tycoon game
      wheat_plants = []
      tomato_plants = []
      carrot_plants = []

      wheat_yield = 0
      tomato_yield = 0
      carrot_yield = 0

      while True:
            print("\n=== Harvest Frenzy Menu ===")
            print("Press Enter to end the turn")
            print("Enter 1 to plant seeds ")
            print("Enter 2 to create recipes")
            print("Enter 3 to view stats")

            print("Enter Q to quit the game")

            choice = input("Choose an option: ")
                  
            if choice == "":
                 #End the turn
                  for wheat in wheat_plants[:]: #Create a shallow copy
                        wheat.growing_time -= 1
                        if wheat.growing_time <= 0:
                              wheat_yield += wheat.yield_amount
                              wheat_plants.remove(wheat)
                              print(f"Harvested {wheat.yield_amount} units of Wheat.")

                  for tomato in tomato_plants[:]: #Create a shallow copy
                        tomato.growing_time -= 1
                        if tomato.growing_time <= 0:
                              tomato_yield += tomato.yield_amount
                              tomato_plants.remove(tomato)
                              print(f"Harvested {tomato.yield_amount} units of Tomato.")


                  for carrot in carrot_plants[:]: #Create a shallow copy
                        carrot.growing_time -= 1
                        if carrot.growing_time <= 0:
                              carrot_yield += carrot.yield_amount
                              carrot_plants.remove(carrot)
                              print(f"Harvested {carrot.yield_amount} units of Carrot.")

            elif choice == "1":
                  #Plant seeds
                  print("Choose a crop to plant:")
                  print("1. Wheat (10 coins)")
                  print("2. Tomato (15 coins)")
                  print("3. Carrot (12 coins)")
                  crop_choice = input("Enter the number of the crop: ")
                  if crop_choice == "1":
                        if Farm.money >= 10:
                              wheat = Wheat()
                              wheat.plant_seed()
                              wheat_plants.append(wheat)
                              wheat_yield += wheat.yield_amount
                              print("Planted Wheat")
                        else:
                              print("Not enough money to plant Wheat")

                  elif crop_choice == "2":
                        if Farm.money >= 15:
                              tomato = Tomato()
                              tomato.plant_seed()
                              tomato_plants.append(tomato)
                              tomato_yield += tomato.yield_amount
                              print("Planted Tomato")
                        else:
                              print("Not enough money to plant Tomato")

                  elif crop_choice == "3":
                        if Farm.money >= 12:
                              carrot = Carrot()
                              carrot.plant_seed()
                              carrot_plants.append(carrot)
                              carrot_yield += carrot.yield_amount
                              print("Planted Carrot")
                        else:
                              print("Not enough money to plant Carrot")
                  else:
                        print("Invalid choice")

            elif choice == "2":
                  #Create recipes
                  print("Choose a recipe to create:")
                  print("1. Bread (3 Wheat)")
                  print("2. Salad (2 Tomato, 2 Carrot)")
                  print("3. Vegetable Stew (2 Wheat, 1 Tomato, 1 Carrot)")
                  recipe_choice = input("Enter the number of the recipe: ")
                  if recipe_choice == "1":
                        if wheat_yield >= 3:
                              Farm.money += 30
                              wheat_yield -= 3
                              print(f"Made Bread. Sold for 30 coins.")
                        else:
                              print("Not enough Wheat to make Bread.")

                  elif recipe_choice == "2":
                       if tomato_yield >= 2 and carrot_yield >= 2:
                             Farm.money += 50
                             tomato_yield -= 2
                             carrot_yield -= 2
                             print(f"Made Salad. Sold for 50 coins.")
                       else:
                             print("Not enough ingredients to make Salad.")

                  elif recipe_choice == "3":
                       if wheat_yield >= 2 and tomato_yield >= 1 and carrot_yield >= 1:
                             Farm.money += 70
                             wheat_yield -= 2
                             tomato_yield -= 1
                             carrot_yield -= 1
                             print(f"Made Vegetable. Sold for 70 coins.")
                       else:
                            print("Not enough ingredients to make Vegetable Stew.")

                  else:
                        print("Invalid choice")

            elif choice == "3":
                  Farm.view_stats(wheat_yield, tomato_yield, carrot_yield)

            elif choice == "Q":
                  #Quit the game
                  print("Quitting the game. Goodbye!")
                  break

            else:
                  print("Invalid option. Please try again.")

##Run the game
main()

            
