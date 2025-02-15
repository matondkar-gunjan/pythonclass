import random
rand_num1 = random.randint(1,10)
rand_num2 = random.randint(1,10)
def max_of_two(x,y):
      if x > y:
            return x
      else:
            return y
max = max_of_two(rand_num1, rand_num2)
print("First random number is: " + str(rand_num1) + "\nSecond random number is:" + str(rand_num2) + "\nThe bigger number is " + str(max))
