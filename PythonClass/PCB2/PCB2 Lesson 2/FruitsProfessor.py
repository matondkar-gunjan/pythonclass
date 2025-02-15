import time
playerList = []
isFruit = []
fruitList = ["APPLE", "BANANA", "ORANGE", "GRAPE"]
gameStart = True
count = 0

for x in range(len(fruitList)):
      player = input("Input Player " + str(x+1) + "'s name: ").capitalize()
      playerList.append(player)


print("Welcoeme to the Fruit Professor Playoff!")
print("May the best fruitist win")
time.sleep(1)

while gameStart:
      print(playerList[count%len(playerList)], "'s turn.")
      fruit = input("Enter a fruit name: ").upper()
      time.sleep(1)
      
      if fruit in isFruit:
            print(fruit, "is a fruit!")
            isFruit.remove(fruit)
      else:
            print(fruit, "is not a fruit!")
            print(playerList[count%len(playerList)], "have lost!")
            time.sleep(1)
            
            
      if fruit in fruitList:
            print(fruit, "is already in the list.")
            print(playerList[count%len(playerList)], "have lost!")
            playerList.remove(playerList[count%len(playerList)])
            time.sleep(1)
            
      else:
            fruitList.append(fruit)
            count += 1

      if len(playerList) == 1:
            print(fruitList)
            print(playerList[0], "is our Fruits Professor!")
            gameStart = False
