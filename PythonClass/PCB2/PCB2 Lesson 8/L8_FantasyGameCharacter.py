import random
def set_attributes(role):
      if role == "warrior":
            strength = random.randint(8, 12)
            magic = random.randint(1, 3)
      elif role == "mage":
            strength = random.randint(1, 3)
            magic = random.randint(8, 12)
      elif role == "rogue":
            strength = random.randint(5, 9)
            magic = random.randint(3, 7)

      return strength + magic
def calculate_power(total_attributes, level):
      power = total_attributes * level
      return power
def create_character(name, role, level):
      total_attributes = set_attributes(role)
      power = calculate_power(total_attributes, level)
      print("Character Name:", name)
      print("Role:", role)
      print("Total Attributes:", total_attributes)
      print("Power Level:", power)
name = input("Enter the character's name: ")
role = input("Choose the character's role(Warrior, Mage, Rogue): ").lower()
level = int(input("Enter the character's level (positive integer ): "))
create_character(name, role, level)
