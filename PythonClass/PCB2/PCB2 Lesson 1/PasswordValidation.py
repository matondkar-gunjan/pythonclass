x = True
while x:
      upper = False
      lower = False
      symbol = False
      password = input("Enter Password: ")
      if len(password) >= 6 and len(password)<= 16:
            for letter in password:
                  if letter.isupper():
                        upper = True
                  elif letter.islower():
                        lower = True
                  elif letter == "$" or letter == "#" or letter == "@":
                        symbol = True
            if upper and lower and symbol:
                  print("Your password is valid")
                  x = False

            else:
                  print("Your password is invalid")
      else:
            print("Your password is invalid")
