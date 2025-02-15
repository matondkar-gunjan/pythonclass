name=input("What is your name?\n")
sport=input("What is your favourite sport?\n").lower()
players=int(input("How many players in the team\n"))
if sport == "cricket":
      score=10*players
      print("If each player scores 10 runs, the team score is",score)
else:
      print("I don't know the rules of this game")
