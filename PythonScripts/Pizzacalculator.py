#AtlantaPizza.py - a simple pizza cost calculator

#Ask user for the number of pizza they want and save the value in variable
numberofpizza = eval(input("How many pizzas do you want?\n"))

#Ask user for the type of pizza they want and save the value in variable
pizzatype = input("What is the pizza type do you want?\n")

while pizzatype not in ['pan', 'personal', 'regular', 'large']:
      print("\nYou have chosen an incorrect option.")
      print("Please select from the following option:")
      print('pan,', 'personal,', 'regular,', 'large,')
      pizzatype = (input("Option chosen:")).lower()

if pizzatype == 'pan':
      costperpizza = 2
elif pizzatype == 'personal':
      costperpizza = 3
elif pizzatype == 'regular':
      costperpizza = 5
'''
#Ask user to put the cost of pizza and save the value in variable
costperpizza = eval(input("How much does each pizza cost?\n"))
'''

#Calculate the total amount before tax user need to pay
subtotal = numberofpizza * costperpizza

#Ask user the rate of sales tax and save the value in variable
salestax = eval(input("\nWhat is the sales tax rate in percent?\n"))
tax_rate = salestax / 100

#What is the sales tax owed for the pizza and save the value in variable
sales_tax_rate = subtotal * tax_rate

#Calculate the total amount user needs to pay and save the value in variable
totalamount = subtotal + sales_tax_rate

#Show the user the total amount user needs to pay including tax
print("The total cost of pizza is $",totalamount,sep="")
print("This includes a sales tax of $",sales_tax_rate,sep="")
