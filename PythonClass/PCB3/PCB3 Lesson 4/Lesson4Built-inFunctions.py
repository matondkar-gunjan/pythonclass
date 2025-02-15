#Example 1: sum() function

print(sum([1, 2, 3, 4])) #Sum of list elements 
print(sum((10, 20))) #Sum of tuple elements

#Example 2: abs() function

print(abs(-10)) #Absolute value of an integer
print(abs(-2.5)) #Absolute value of a float

#Example 3: min() function

#Minimum of integers
print(min(5, 2, 9, 1))

#Minimum of strings
print(min("apple", "orange", "banana"))

#Minimum of list of lists based on the sum of elements

lists = [[10, 5], [4, 0], [7, 8]]
print(min(lists, key=sum))
