cards = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
suits = ["diamond", "club", "heart", "spade"]
import random
my_card = random.choice(cards)
your_card = random.choice(cards)
my_suit = random.choice(cards)
your_suit = random.choice(cards)

print("My card: " + my_card + " of " + my_suit + " Your card: " + your_card + " of " + your_suit)

if(cards.index(my_card) > cards.index(your_card)):
   print("I win!")
elif(cards.index(my_card) < cards.index(your_card)):
      print("I lose!")
elif(cards.index(my_card) == cards.index(your_card)):
      if(suits.index(my_suit) > suits.index(your_suit)):
            print("I win!")
      elif(suits.index(my_suit) < suits.index(your_suit)):
            print("I lose!")
      else:
            print("Tie")

x = ""
while x == "":
      my_card = random.choice(cards)
      your_card = random.choice(cards)
      my_suit = random.choice(cards)
      your_suit = random.choice(cards)

      print("My card: " + my_card + " of " + my_suit + " Your card: " + your_card + " of " + your_suit)

      if(cards.index(my_card) > cards.index(your_card)):
         print("I win!")
      elif(cards.index(my_card) < cards.index(your_card)):
            print("I lose!")
      elif(cards.index(my_card) == cards.index(your_card)):
            if(suits.index(my_suit) > suits.index(your_suit)):
                  print("I win!")
            elif(suits.index(my_suit) < suits.index(your_suit)):
                  print("I lose!")
            else:
                  print("Tie")
      x = input("Press [Enter] to continue. Any key to exit.")
      
