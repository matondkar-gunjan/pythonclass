def divide_numbers():
      try:
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            result = numerator / denominator
            print("The result of the division is", result)
      except ZeroDivisionError:
            print("Oops! You cannot divide by zero. Please try again with a different number.")
divide_numbers()
