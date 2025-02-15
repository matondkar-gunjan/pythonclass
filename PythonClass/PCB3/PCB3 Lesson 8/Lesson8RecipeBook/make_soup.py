from Lesson8Kitchen import cut_vegetables, season_food

def make_croutons():
      print("\n")
      bread_type = input("Enter the type of bread to use for the croutons: ")
      crouton_size = input("Enter the crouton size (e.g., small, medium, large): ")
      print(f"Cutting {bread_type} bread for {crouton_size} croutons and toasting them...")
      
      
def make_soup():
      print("Starting to prepare soup with croutons...")
      cut_vegetables()# Cut the vegetables for the soup
      season_food() # Season the soup
      make_croutons() # Prepare croutons
      print("Soup with croutons is ready to serve")

make_soup()
