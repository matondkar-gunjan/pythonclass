from Ninja import Ninja
import random

class FireNinja(Ninja):
      def __init__(self, name, chakra, health, attack_power, healing_ability, ignite_chance):
            super().__init__(name, chakra, health, attack_power, healing_ability)
            self.ignite_chance = ignite_chance
            self.resilience = 0.2

      def attack(self):
            if self.cooldown > 0:
                  print(f"{self.name} is recovering and can't attack yet! ({self.cooldown} turns left)")
                  return 0

            if self.chakra >= 10:
                  damage = self.attack_power
                  self.chakra -= 10
            else:
                  damage = self.attack_power / 2
                  self.chakra -= 5

            if random.random() < self.ignite_chance:
                  ignite_damage = damage // 2
                  print(f"{self.name} ignites the enemy, dealing an extra {ignite_damage} damage over time!")
                  damage += ignite_damage

            self.cooldown = 2
            print(f"{self.name} attacks with power {damage}")
            return damage
      
      def receive_damage(self, damage, defending = False):
            if random.random() < self.resilience:
                  damage *= 0.5
                  print(f"{self.name}'s resilience reduces the damage by half!")

            if defending == True:
                  damage *= 0.5
                  print(f"{self.name} defends and reduces the damage to {damage}.")

            self.health -= damage
            if self.health <= 0:
                  print(f"{self.name} has been defeated.")
            else:
                  print(f"{self.name} receives {damage} damage.")
                  
                  

      
