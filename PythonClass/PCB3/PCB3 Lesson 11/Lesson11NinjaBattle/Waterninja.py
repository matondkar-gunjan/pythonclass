from Ninja import Ninja
class WaterNinja(Ninja):
      def __init__(self, name, chakra, health, attack_power, healing_ability, water_shield):
            super().__init__(name, chakra, health, attack_power, healing_ability)
            self.water_shield = water_shield
            

      def attack(self):
            if self.cooldown > 0:
                  print(f"{self.name} is recovering and can't attack yet! ({self.cooldown} turns left)")
                  return 0

            if self.chakra >= 15:
                  enhanced_damage = self.attack_power + int(self.attack_power * self.water_shield)
                  self.chakra -= 15
                  print(f"{self.name} uses the water shield to enhance the attack!")
            else:
                  damage = self.attack_power // 2
                  self.chakra -= 5

            self.cooldown = 2
            print(f"{self.name} attacks with power {enhanced_damage}")
            return enhanced_damage
      
      def receive_damage(self, damage, defending = False):
            reduced_damage = damage * (1 - self.water_shield)

            print(f"{self.name} uses water shield to reduce incoming damage by {int(self.water_shield * 100)}%")
            
            
            if defending == True:
                  damage *= 0.5
                  print(f"{self.name} defends and reduces the damage to {reduced_damage}.")

            self.health -= reduced_damage
            if self.health <= 0:
                  print(f"{self.name} has been defeated.")
            else:
                  print(f"{self.name} receives {reduced_damage} damage.")

                  
                  
