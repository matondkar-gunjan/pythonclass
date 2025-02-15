import random
x = True
rand_num = random.randint(1,100)
while x:
      print("Searching coordiates: ", rand_num)
      if rand_num == 25:
            x = False
            print("Congratulations! You've found the treasure at coordinate 25!")
      rand_num = random.randint(1,100)
