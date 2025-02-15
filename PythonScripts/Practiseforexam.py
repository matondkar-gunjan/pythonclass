orig_num_of_books = 10
while orig_num_of_books >= 0:
      borrowed = int(input("How many books would you like to borrow?: "))
      if borrowed < orig_num_of_books:
            orig_num_of_books = orig_num_of_books - borrowed    
            print("Number of books borrowed: ", borrowed)
            print("Number of books left: ", orig_num_of_books)
      else:
            print("There are not enough books")
            break
