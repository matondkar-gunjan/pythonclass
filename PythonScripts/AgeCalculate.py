name=input("What is your name?\n")
age=int(input("How old are you?\n"))
#factor=int(input("What is the factor?\n"))
for x in range(10):
      #x=x+1
      if x == 0:
            newage=x+age
            print("You are currently",newage,"years old",end=",")
      else:
            newage=x+age
            print("In",x,"years you will be",newage,"years old")
