import random
from Fireninja import FireNinja
from Waterninja import WaterNinja
def create_ninja():
      name = input("Enter the name of your ninja: ")
      chakra = int(input("Enter chakra of your ninja: "))
      health = int(input("Enter health of your ninja: "))
      attack_power = random.randint(50, 100)
      healing_ability = random.randint(20, 40)
      ignite_chance = random.random()
      water_shield = random.random()

      print("Choose your ninja type:")
      print("1. Fire Ninja")
      print("2. Water Ninja")
      choice = int(input("Enter your choice (1 or 2): "))

      if choice == 1:
            return FireNinja(name, chakra, health, attack_power, healing_ability, ignite_chance), 2
      elif choice == 2:
            return WaterNinja(name, chakra, health, attack_power, healing_ability, water_shield), 1
      else:
            print("Invalid choice! Defaulting to Fire Ninja.")
            ignite_chance = 0.2
            return FireNinja(name, chakra, health, attack_power, healing_ability, ignite_chance), 2
            
