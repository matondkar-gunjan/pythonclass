import random
computer = [0,0,0,0,0]
player = [0,0,0,0,0]

for i in range(5):
      computer[i] = random.randint(1,6)
computer.sort()

for i in range(5):
      player[i] = random.randint(1,6)
player.sort()


print("You rolled:" + str(player))
print("Computer rolled:" + str(computer))

if player[0] == player[4]:
      ("Player got Yahtzee, Player win !")

if computer[0] == computer[4]:
      print("Computer and Player got Yahtzee, it's a draw!")

elif computer[0] == computer[3] and player[0] == player[4]:
      print("Computer got Four of a kind, Player got Yahtzee, Player Win")
elif computer[0] == computer[2] and player[0] == player[4]:
      print("Computer got Three of a kind, Player got Yahtzee, Player Win")
else:
      print("Computer did not get any of the three, Player got Yahtzee, Player Win")
