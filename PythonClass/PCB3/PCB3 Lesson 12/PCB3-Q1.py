class BookCollection:
      total_books = 0
      
      def __init__(self, title, author, is_available):
            self.title = title
            self.author = author
            self.is_available = is_available
            BookCollection.total_books += 1

     
      def book_details(self):
            print("\n")
            print("Title: " + self.title)
            print("Author: " + self.author)

      def check_availability(self):
            if self.is_available:
                 print(f"{self.title} is available")
            else:
                  print(f"{self.title} is not available")

                  
      
      
book1 = BookCollection("To Kill a Mockingbird", "Harper Lee", True)

book2 = BookCollection("1984", "George Orwell", False)

book1.book_details()
book1.check_availability()

book2.book_details()
book2.check_availability()

print("\n")
print("Total number of books in the collection:", BookCollection.total_books)


    
      
           
     
      






