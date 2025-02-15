def access_list_element():
      my_list = [1, 2, 3, 4, 5]
      try:
            index = int(input("Enter an index to access an element: "))
            element = my_list[index]
            print("The element at index", index, "is", element)
      except IndexError:
            print("Oops! The index is out of range. Please try again with a valid index.")
access_list_element()      
