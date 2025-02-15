from Assassin import Assassin
from Healer import Healer
from Marksman import Marksman

def main():
      print("Welcome to the game")
      print("Choose your character for the match")
      print("1. Assassin - Special ability: Stealth Attack")
      print("2. Healer - Special ability: Heal Allies")
      print("3. Marksman - Special ability: Precision Shot")
      choice = input("Enter the number of your choice (1,2,3): ")

      if choice == "1":
            selected_character = Assassin()
      elif choice == "2":
            selected_character = Healer()
      elif choice == "3":
            selected_character = Marksman()
      else:
            selected_character = None


      if selected_character:
            print(f"You have chosen: {selected_character.name} the {selected_character.role}")
            print("Entering the match...")
            selected_character.perform_ability()
            selected_character.special_attack()
      else:
            print("Invalid choice. Please run the program again and choose a valid option")



if __name__=="__main__":
      main()
