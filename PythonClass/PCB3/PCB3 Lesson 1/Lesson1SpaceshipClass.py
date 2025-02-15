class Spaceship:
      def __init__(self, name, firepower):
            self.name = name
            self.firepower = firepower
name1 = input("Enter the name of spaceship1: ")
firepower1 = int(input("Enter the firepower of spaceship1: "))
spaceship1 = Spaceship(name1, firepower1)

name2 = input("Enter the name of spaceship2: ")
firepower2 = int(input("Enter the firepower of spaceship2: "))
spaceship2 = Spaceship(name2, firepower2)

name3 = input("Enter the name of spaceship3: ")
firepower3 = int(input("Enter the firepower of spaceship3: "))
spaceship3 = Spaceship(name3, firepower3)

print("Spaceship 1 - Name: ", name1, "Firepower:", firepower1)
print("Spaceship 2 - Name: ", name2, "Firepower: ", firepower2)
print("Spaceship 3 - Name: ", name3, "Firepower: ", firepower3)

total_fleet_firepower = firepower1 + firepower2 + firepower3
print("Total fleet firepower: ", total_fleet_firepower)
if total_fleet_firepower <= 300:
      print("Your fleet needs more upgrades")
elif total_fleet_firepower > 300:
      print("Your fleet is strong enough to protect the galaxy")
      
else:
      print("Your fleet is too weak, you need more ships")
      

