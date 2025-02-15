import random
def ability_generator(abilities, affinities, character_count):
      characters = []
      for i in range(character_count):
            ability = random.choice(abilities)
            affinity = random.choice(affinities)
            character = " Ability - " + ability + ", Elemental Affinity - " + affinity
            characters.append(character)
      return(character)

print("Welcome to the Realm of Special Abilities!")
abilities = ["Fireball", "Telekinesis", "Invisibility", "Healing Touch", "Thunderstorm"]
affinities = ["Fire", "Water", "Earth", "Air", "Lightning"]
character_count = int(input("Enter the number of characters to generate abilities for: "))
character_abilities = ability_generator(abilities, affinities, character_count)
print("Here are the special abilities that shall empower the heroes and villains of your tale:")
for i in range(len(abilities)):
      print("Character " + str(i+1) + character_abilities)
