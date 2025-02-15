class MinecraftCharacter:
      def __init__(self, name, health, inventory_size):
            self.name = name
            self.health = health
            self.inventory_size = inventory_size

      def check_profile(self):
            print("\n")
            print("Before gearing up: ")
            print("Name: ", self.name)
            print("Health: ", self.health)
            print("Inventory size: ", self.inventory_size)
            
      def after_gearing_up(self):
            pass
      
class Warrior(MinecraftCharacter):
      def __init__(self, name = "Warrior Steve" , health = 150, inventory_size = 10, attack_power = 20, weapon = "Sword"):
            super().__init__(name, health, inventory_size)
            self.weapon = weapon
            self.attack_power = attack_power
            
      

      def after_gearing_up(self):
            print("\n")
            print(f"{self.name} is gearing up for battle with a {self.weapon}!")
            self.attack_power += 40
            self.health += 50
            print(f"Attack power increased to {self.attack_power}!")
            print(f"Health increased to {self.health}!")
            print("\n")
            print("After gearing up:")
            print("Name: ", self.name)
            print("Health: ", self.health)
            print("Inventory Size: ", self.inventory_size)
            print("Attack power: ", self.attack_power)

     
print("\n")
class Builder(MinecraftCharacter):
      def __init__(self, name = "Builder Alex", health = 100, inventory_size = 20, tools = "Pickaxe", building_speed = 40):
            super().__init__(name, health, inventory_size)
            self.tools = tools
            self.building_speed = building_speed

      def after_gearing_up(self):
            print("\n")
            print(f"{self.name} is equipping a {self.tools} for building!")
            self.building_speed += 40
            self.inventory_size += 10
            print(f"Building speed increased to {self.building_speed} blocks/min!")
            print(f"Inventory size increased to {self.inventory_size}!")
            print("\n")
            print("After gearing up:")
            print("Name: ", self.name)
            print("Health: ", self.health)
            print("Inventory Size: ", self.inventory_size)
            print("Building Speed: ", self.building_speed)




warrior1 = Warrior()
builder1 = Builder()

warrior1.check_profile()
builder1.check_profile()

warrior1.after_gearing_up()
builder1.after_gearing_up()
            


            
            

      
