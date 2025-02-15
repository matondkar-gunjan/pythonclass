import time
animalList = []
number = int(input("How many animals do you want to input? "))
while len(animalList) < number:

      animal = input("What animals do you like? ")
      animalList.append(animal)

print(animalList)
time.sleep(1)
print("Thank you for sharing! Let's start the game!")
clear()
print("Welcome to Guess My Favourite Animal Game!")

x = True
while x:
      animal = input("What animals do you like? ")
      if animal in animalList:
            animalList.remove(animal)
      else:
            print("Please try again! You have ", len(animalList), " animals left to guess.")
            time.sleep(1)
            clear()

      
