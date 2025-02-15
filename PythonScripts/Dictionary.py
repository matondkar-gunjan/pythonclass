farm_animals = {
      "cow": 10,
      "chicken": 15,
      "pig": 20
}
print(farm_animals)
farm_animals["cow"] = 15
print("\nUpdating number of farm animals")
print(farm_animals)
print("Is 'cow' in dictionary", "cow" in farm_animals)
print("Is 'lion' in dictionary", "Lion" in farm_animals)
print("\nPrint dictionary")
for animal,quantity in farm_animals.items():
      print(animal, ":", quantity)
