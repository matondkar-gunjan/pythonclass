class Computation:
      def __init__(self):
            pass
            
      def factorial(self, n):
            print("\nCalculating factorial of number n")
            j = 1
            for i in range(1, n + 1):
                  j = i
            return j
      
      def sum(self, n):
            print("\Calculating Sum of first n number")
            j = 1
            for i in range(1, n + 1):
                  j = i
            return j

      def tableMult(self, k):
            print("\nRetrieve time table for n")
            for i in range(1, 13):
                  print(i, "x", k, "=", i * k)

      def testPrim(self, n):
            print("\nChecking if number n is a prime number")
            j = 0
            for i in range(1, n + 1):
                  if(n % i == 1):
                        j = j + 1
                  if (j == 2):
                        return True
                  else:
                        return False
                  
      def display(self, n):
            print("Calculating factorial of number n: ", self.factorial(n))
            print("Calculating sum of first n number: ", self.sum(n))
            print("Retrieve time table for n: ", self.tableMult(n))
            print("Checking if number n is a prime number: ", self.testPrim(n))
myNum = Computation()
myNum.display(9)

