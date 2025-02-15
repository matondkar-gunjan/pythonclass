def convert_to_integer():
      try:
            user_input = input("Enter a string to convert to an integer: ")
            integer_value = int(user_input)
            print("The integer value is", integer_value)
      except ValueError:
            print("Oops! That's not a valid number. Please enter a valid integer.")
convert_to_integer()
