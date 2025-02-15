import time
def recur_factorial(m):
      results = 1
      if m <= 1:
            return 1
      else:
            return m*recur_factorial(m-1)
m = 0
print("\nRecursive factorial function")
while m < 10:
      start = time.time()
      result = recur_factorial(m)
      m = m + 1
      end = time.time()
      print(f'The time taken to run the program is {end-start:.10f} and the result of factorial {m} is {result}')
