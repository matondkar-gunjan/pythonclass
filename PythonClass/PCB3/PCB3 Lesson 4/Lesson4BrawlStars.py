import random

class Brawler:
      def __init__(self, name, health, attack_power):
            self.name = name
            self.health = health
            self.attack_power = attack_power
            
      def attack(self, opponent):
            print("I'm " + self.name + " and I attack " + self.attack_power + "!")
            self.health -= self.attack_power
            
      def show_status(self):
            print("Name: ", self.name)
            print("Health: ", str(self.health))
            print("Attack power: ", str(self.attack_power))


class Shelly(Brawler):
      def __init__(self):
            super().__init__(name = "Shelly", health = 100, attack_power = 20)
            self.range = int(input("Enter the range for Shelly: "))
            
      def attack(self, opponent):
            #Add new line for better readability
            print("\n")
            print("I'm " + self.name + " and I fire a wide-spread shotgun blast!")
            print("Range: " + str(self.range))
            #Increase attack power by 1% per unit of range
            new_attack_power = self.attack_power * (1 + self.range/100.0)
            #Shelly's attack has a 30% chance to deal double damage
            if self.range <= 0.3:
                  damage = new_attack_power * 2
                  print("Critical hit!")
            else:
                  damage = new_attack_power
            opponent.health -= damage
            print(opponent.name + " takes " + str(damage) + " damage")


class Colt(Brawler):
      def __init__(self):
            super().__init__(name = "Colt", health = 120, attack_power = 25)
            self.ammo = int(input("Enter the ammo for Colt:"))

      def attack(self, opponent):
            print("\n")
            print("I'm " + self.name + " and I shoot a rapid-fire burst of bullets at " + opponent.name + "!")
            print("Ammo: " + str(self.ammo))
            #Colt's attack consumes 1 ammo
            if self.ammo > 0:
                  opponent.health -= self.attack_power
                  self.ammo -= 1
                  print(opponent.name + " takes " + str(self.attack_power) + " damage!")
                  print(self.name + " has " + str(self.ammo) + " ammo left.")
            else:
                  print(self.name + " has no ammo left")

shelly = Shelly()
colt = Colt()
brawlers = [shelly, colt]

while shelly.health > 0 and colt.health > 0:
      attacker = random.choice(brawlers)
      if attacker == colt:
            defender = shelly
      else:
            defender = colt
      attacker.show_status()
      attacker.attack(defender)
      #If Colt has run out of ammo after attack, break out of the loop
      if attacker.name == "Colt" and attacker.ammo == 0:
            print(attacker.name, " has run out of ammo!")
            break
      #If defender is defeated after attack, break out of the loop
      if attacker.health <= 0 or defender.health <0:
            break
      defender.show_status()
      defender.attack(attacker)

print("\n")
print("Battle Over! Final Results:")
for brawler in brawlers:
      brawler.show_status()
      
#Print the winner using a loop
for brawler in brawlers:
      if brawler.health > 0:
            print("\n")
            print(brawler.name + " has won the fight!")
            break
