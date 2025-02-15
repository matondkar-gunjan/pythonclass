pet_inventory = {
      "Dog": "available for adoption",
      "Cat": "available for adoption",
      "Rabbit": "available for adoption"
}
print("\nPart 1: Initial Inventory Setup")
print("\nPet Center Inventory: ")
for animal, availability in pet_inventory.items():
      print(animal, ":", availability)
pet_inventory["Dog"] = "not available for adoption"
print("\nPart 2: Inventory Update")
print("Updated Pet Center Inventory: ")
for animal, availability in pet_inventory.items():
      print(animal, ":", availability)

del pet_inventory["Cat"]
print("\nPart 3: Pet Adoption")
print("Updated Pet Center Inventory: ")
for animal, availability in pet_inventory.items():
      print(animal, ":", availability)

print("\nPart 4: Check for pets")
print("Is 'Rabbit' available for adoption?", "Rabbit" in pet_inventory)
print("Is 'Bird' available for adoption?", "Bird" in pet_inventory)


print("\nPart 5: Print inventory")
print("\nPet Center Inventory:")
for animal, avalibility in pet_inventory.items():
      print(animal, ":", avalibility)
