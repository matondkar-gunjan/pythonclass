#Ask the user for their name and save in variable
name=input("What is your name?\n")

#Print the name variable 100 times
for x in range(100):
      if (x%2) == 0:
            print(name, end="+")
      elif x == 99:
            print (name)
      else:
            print(name, end=" rules! ")
            
