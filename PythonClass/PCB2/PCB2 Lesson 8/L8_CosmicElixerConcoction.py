import random
def potion_brewer(cosmic_ingredients, potion_count):
      potions = []
      for i in range(potion_count):
            potion = "Cosmic Elixer of " + random.choice(cosmic_ingredients)
            potions.append(potion)
      return(cosmic_ingredients)
print("Welcome to the Intersteller Academy of Alchemy!")
cosmic_ingredients = ["Stardust", "Galactic Essence", "Nebula Nectar", "Celestial Spice", "Lunar Lotus"]
potion_count = int(input("Enter the number of potions to generate: "))
cosmic_elixers = potion_brewer(cosmic_ingredients, potion_count)
print("You have successfully brewed the follwing cosmic elixers:")
for potion in cosmic_elixers:
      print(potion)
