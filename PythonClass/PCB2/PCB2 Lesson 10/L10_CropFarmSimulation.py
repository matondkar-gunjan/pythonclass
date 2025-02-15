crop_farm = {
      "Wheat": 50,
      "Corn": 30,
      "Carrot": 40
}
print("Part 1: Initial Inventory Setup")
print(crop_farm)

crop_farm["Wheat"] = 60
print("\nPart 2: Inventory Update")
print(crop_farm)

del crop_farm["Corn"]
print("\nPart 3: Crop Harvest")
print(crop_farm)

print("\nPart 4: Check for crops")
print("Is 'Carrot' in the inventory?", "Carrot" in crop_farm)
print("Is 'Potato' in the inventory?", "Potato" in crop_farm)

print("\nPart 5: Print Inventory")
for crop, quantity in crop_farm.items():
      print(crop, ":", quantity)
