pets = ["Bunny", "Puppy", "Kitty", "Parrot"]
spot_number = 1

for pet in pets[:]:
      print(f"{pet} goes to Spot {spot_number}.")
      spot_number += 1
      pets.remove(pet)
