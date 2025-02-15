#my_name="Gunjan"
#my_age=10
#your_name=input("What is your name?\n")
#your_age=input("What is your age?\n")
#print("My name is ",my_name,", and I am ",my_age," years old.",sep="")
#print("Your name is ",your_name,", and you are ",your_age," years old.",sep="")
#my_name=your_name
#print(my_name)
#num=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*100
#print(num)
pizza_type=str(input("What type of pizza would you like?\n"))
#num_of_slice=8
personal_slice=4
regular_slice=6
large_slice=12
if pizza_type=="personal":
      cost_of_slice=10/personal_slice
      print("The cost of a ", pizza_type," slice is $",cost_of_slice,sep="")
elif pizza_type=="regular":
      cost_of_slice=10/regular_slice
      print("The cost of a ", pizza_type," slice is $",cost_of_slice,sep="")
elif pizza_type=="large":
      cost_of_slice=10/large_slice
      print("The cost of a ", pizza_type," slice is $",cost_of_slice,sep="")
else:
      print("You have chosen the wrong pizza type")
