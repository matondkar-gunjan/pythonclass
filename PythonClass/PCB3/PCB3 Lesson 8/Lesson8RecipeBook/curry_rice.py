from Lesson8Kitchen import marinate_meat, season_food, add_herbs

def cook_rice():
      print("\n")
      rice_type = input("Enter the type of rice you want to use: (e.g., basmati, jasmine): ")
      cook_time = int(input("Enter the cooking time for the rice in minutes: "))
      print(f"Cooking {rice_type} rice for {cook_time} minutes...")
      
      
def make_curry_rice():
      print("Starting to prepare Curry Rice...")
      marinate_meat()# Marinate the meat
      add_herbs() # Add herbs for flavor
      season_food() # Season the curry
      cook_rice() # Prepare the rice
      print("Curry Rice is ready to serve")

make_curry_rice()
