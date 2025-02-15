class GameCharacter:
      def __init__(self, name, power):
            self.name = name
            self.power = power
name1 = input("Enter the name of the first character: ")
power1 = input("Enter the power of the first character: ")
character1 = GameCharacter(name1, power1)

name2 = input("Enter the name of the second character: ")
power2 = input("Enter the power of the second character: ")
character2 = GameCharacter(name2, power2)

print("First character's name:", name1)
print("Second character's name:", name2)

total_power = int(power1) + int(power2)
print("Total power:", total_power)
if total_power == 220:
      print("You can go slay the dragon")
else:
      print("You need more training")
