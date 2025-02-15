class MarvelHero:
      def __init__(self, name, health, attack_power):
            self.name = name
            self.health = health
            self.attack_power = attack_power
            
      def BeforeSuitUp(self):
            print("Checking profile:")
            print("Name: ", self.name)
            print("Health: ", self.health)
            print("Attack power: ", self.attack_power)
            
      def AfterSuitUp(self):
            print(self.name + " is wearing a normal suit for battle! ")
            
class IronMan(MarvelHero):
      def __init__(self, defense = 50, suit = "iron"):
            super().__init__(name = "Iron Man", health = 100, attack_power = 10)
            self.suit = suit
            self.defense = defense
            
      def check_profile(self):
            super().BeforeSuitUp()
            print("Defense: ", self.defense)

      def suit_up(self):
            print(self.name + " suits up in his " + self.suit + " Iron Man suit!")
            print("Tony gets his iron suit, he increases defense by 40 and attack power by 90")

            print("\n")
            self.attack_power += 90
            self.defense += 40
            self.check_profile()

class Thor(MarvelHero):
      def __init__(self, strength = 0, weapon = "Mjolnir"):
            super().__init__(name = "Thor", health = 300, attack_power = 100)
            self.strength = strength
            self.weapon = weapon

      def check_profile(self):
            super().BeforeSuitUp()
            print("Strength: ", self.strength)

      def suit_up(self):
            print(self.name + " wields his mighty hammer " + self.weapon + "!")
            print("Thor gets his hammer, he increases attack power by 100 and strength by 500!")

            print("\n")
            self.attack_power += 100
            self.strength += 500
            self.check_profile()

iron_man = IronMan()
thor = Thor()
heroes = [iron_man, thor]

for hero in heroes:
      print("Before suiting up:")
      hero.check_profile()

      print("\n")
      hero.suit_up()
      print("\n")


      
      
      
