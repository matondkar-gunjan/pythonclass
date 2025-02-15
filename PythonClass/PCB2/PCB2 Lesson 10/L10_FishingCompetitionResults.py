fish_competition = {
      "participant 1": 25,
      "participant 2": 18,
      "participant 3": 30,
      "participant 4": 22,
      "participant 5": 20
}
print("Part 1: Initial Competition Setup")
print(fish_competition)
del fish_competition["participant 3"]
print("\nPart 2: Disqualification")
print(fish_competition)
fish_competition["participant 2"] = 28
fish_competition["participant 4"] = 24
print("\nPart 3: Adjustments")
print(fish_competition)
print("\nPart 4: Announcement")
for participant, weight in fish_competition.items():
      if weight > 20:
            print(participant, "caught a", weight, "kg fish.")
print("\nPart 5: Winner Announcement")
max_weight = -1
winner = ""
for participant in fish_competition:
      if fish_competition[participant] > max_weight:
            max_weight = fish_competition[participant]
            winner = participant
print("The winner is", winner, "with a", max_weight, "kg fish!")
