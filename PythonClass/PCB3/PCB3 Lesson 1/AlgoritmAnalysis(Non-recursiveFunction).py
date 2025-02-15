import time
def factorial(n):
      results = 1
      for i in range(1, n+1):
            results = results * 1
      return results
n = 0
print("Non recursive factorial function")
while n < 10:
      start = time.time()
      result = factorial(n)
      n = n + 1
      end = time.time()
      print(f'The time taken to run the program is {end-start:.10f} and the result of factorial {n} is {result}')
