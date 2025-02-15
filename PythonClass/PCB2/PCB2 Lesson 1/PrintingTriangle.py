number = int(input("How many rows do you want?: "))
pattern = input("What pattern do you want to print [*, ?, #]: ")
i = 0
while i < (number):
      print((i + 1) * pattern)
      i += 1
