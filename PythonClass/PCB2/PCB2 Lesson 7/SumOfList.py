import random
num_list = [0,0,0,0,0]
for x in range(len(num_list)):
      num_list[x] = random.randint(1,10)
def sum(list):
      total = 0
      for x in list:
            total = x + total
      return total
print(num_list)
print("The total value of the list is " + str(sum(num_list)))
