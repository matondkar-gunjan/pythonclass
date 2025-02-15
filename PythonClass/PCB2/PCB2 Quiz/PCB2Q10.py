try:
      numbers = [10, 20, 30, 40, 50]
      print(numbers)
      num1 = input("Enter the first number: ")
      num2 = input("Enter the second number: ")
      result = int(num1) / int(num2)
      print("The result of the division is", result)
      index = int(input("Enter the index of the number you want to access: "))
      print("The number at index", index, "is", numbers[index])
except ZeroDivisionError:
      print("Oops! Division by zero is not allowed.")
except IndexError:
      print("Oops! The index you are trying to access is out of range.")
except ValueError:
      print("Oops! Please enter valid numbers.")
