try:
      ticket_price = 12.5
      number_of_tickets = input("Enter the number of tickets you want to buy: ")
      total_price = ticket_price * int(number_of_tickets)
      print("The total price is", total_price)
except ValueError:
      print("Oops! Please enter a valid number for the tickets")
