def marinate_meat():
      meat_type = input("Enter the type of meat you want to marinate: ")
      time_in_minutes = int(input("Enter marination time in minutes: "))
      print(f"Marinating {meat_type} for {time_in_minutes} minutes...")
      print("\n")
      
def cut_vegetables():
      vegetables = input("Enter the vegetables to cut, separated by commas: ").split(",")
      print("Cutting the follwing vegetables: ")
      for veg in vegetables:
            print(f"- {veg} ")
      print("\n")
      
      
def add_herbs():
      herb_type = input("Enter the type of herb: ")
      amount = int(input("Enter the amount of the herb in grams: "))
      print(f"Adding {amount} g of {herb_type} to the dish.")
      print("\n")

def season_food():
      seasoning_type = input("Enter the type of seasoning: ")
      amount = int(input("Enter the amount of seasoning in grams: "))
      print(f"Adding {amount} g of {seasoning_type} to the dish.")
      
