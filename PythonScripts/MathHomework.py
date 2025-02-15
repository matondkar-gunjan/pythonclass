print("MathHomework.py")

#Ask the user to enter a math problem

problem=input("Enter a math problem, or 'q' to quit: \n")

#Keep going until the user enters 'q' to quit

while (problem != "q"):
      #Show the problem, and the answer using eval()
      print("The answer to ", problem, "is:",eval(problem))
      #Ask for another math problem

      problem=input("Enter another math problem, or 'q' to quit: \n")
      #This loop will keep going until the user enters 'q'
