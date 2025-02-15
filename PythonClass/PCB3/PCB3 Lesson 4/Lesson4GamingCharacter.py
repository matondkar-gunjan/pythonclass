class Character:
      def __init__(self, name, health, strength):
            self.name = name
            self.health = health
            self.strength = strength
            
      def attack(self):
            print(self.name + " attacks with a basic strength of " + str(self.strength))


class Fighter(Character):
      def __init__(self, name, health, strength, weapon):
            super().__init__(name, health, strength)
            self.weapon = weapon
            
      def attack(self):
            print(self.name + " attacks with a " + self.weapon + "!")


class Mage(Character):
      def __init__(self, name, health, strength, magic_power):
            super().__init__(name, health, strength)
            self.magic_power = magic_power
            
      def attack(self):
            print(self.name + " casts a spell with " + str(self.magic_power) + " power!")
            

class Archer(Character):
      def __init__(self, name, health, strength, range):
            super().__init__(name, health, strength)
            self.range = range

      def attack(self):
            print(self.name + " shoots an arrow from " + str(self.range) + " distance!")

            
fighter = Fighter("Thor", 100, 80, "sword")
mage = Mage("Morgana", 60, 40, "fireball")
archer = Archer("Eldrin", 70, 60, "longbow")

#List of characters
characters = [fighter, mage, archer]

#For loop to print attack actions
for character in characters:
      character.attack()
