import random

class Ninja:
      def __init__(self, name, chakra, health, attack_power, healing_ability):
            self.name = name
            self.chakra = chakra
            self.health = health
            self.attack_power = attack_power
            self.healing_ability = healing_ability
            self.cooldown = 0
            self.defend_cooldown = 0

      def attack(self):
            pass
      
      def receive_damage(self, damage, defending = False):
            pass
      
      def heal(self):
            if self.chakra < 5:
                  print(f"{self.name} doesn't have enough chakra to heal.")

                  return
            print(f"{self.name} meditates and restores {self.healing_ability} health")
            self.health += self.healing_ability
            self.chakra -= 5

      def defend(self):
            if self.defend_cooldown > 0:
                  print(f"{self.name} is recovering and can't defend yet! ({self.defend_cooldown} turns left) ")
                  #Indicating that the ninja couldn't defend due to cooldown
                  return False
            print(f"{self.name} is defending! Incoming damage will be reduced.")
            #Set cooldown for defending
            self.defend_cooldown = 2
            return True
      def show_status(self):
            print(f"Ninja: {self.name}")
            print(f"Chakra: {self.chakra}")
            print(f"Health: {self.health}")

      def cooldown_tick(self):
            if self.cooldown > 0:
                  self.cooldown -= 1
            if self.defend_cooldown > 0:
                  self.defend_cooldown -= 1
                  
      
