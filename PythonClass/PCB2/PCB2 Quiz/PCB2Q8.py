animal_habitats = {
      "Savannah": "Lion",
      "Rainforest": "Monkey",
      "Arctic": "Polar Bear"
}
print("\nMethod 1: Looping through keys(habitats):")
for habitat in animal_habitats:
      print("Habitat:", habitat)

print("\nMethod 2: Looping through values(animals):")
for animal in animal_habitats.values():
      print("Animal: ", animal)

print("\nMethod 3: Looping through key-value pairs:")
for habitat, animal in animal_habitats.items():
      print(habitat, ":", animal)
