first_rating = int(input("Enter the rating for the first movie (out of 10): "))
first_rating_again = int(input("Enter another rating for the first movie (out of 10): "))
second_rating = int(input("Enter the rating for the second movie (out of 10): "))
second_rating_again = int(input("Enter another rating for the second movie (out of 10): "))
def average_rating(a, b):     
      aver_rating = a + b/2
      return(aver_rating)
var1 = average_rating(first_rating, first_rating_again)
var2= average_rating(second_rating, second_rating_again)
if var1 > var2:
      print("The first movie has a higher rating")
else:
      print("The second movie has a higher rating")

