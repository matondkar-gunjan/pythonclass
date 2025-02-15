num_of_blaze_rods = int(input("Enter the number of blaze rods available: "))
amount_of_blaze_powder = num_of_blaze_rods * 2
num_of_cobblestones = int(input("Enter the number of cobblestones available: "))
num_of_brewing_stands = num_of_cobblestones / 3
def blaze_powder_crafter(): 
      return amount_of_blaze_powder
def brewing_stand_crafter():
      return num_of_brewing_stands
def strength_potion_crafter():
      if amount_of_blaze_powder > num_of_brewing_stands:
            potion = int(num_of_brewing_stands)
            print("You can craft a maximum of ", potion , " Potion(s) of Strength")
      elif num_of_brewing_stands > amount_of_blaze_powder:
            potion = int(amount_of_blaze_powder)
            print("You can craft a maximum of ", int(potion) , " Potion(s) of Strength")
      else:
            if amount_of_blaze_powder == num_of_brewing_stands:
                  potion = num_of_brewing_stands
                  print("You can craft a maximum of ",int(potion) , " Potion(s) of Strength")
blaze_powder_crafter()
brewing_stand_crafter()
strength_potion_crafter()
