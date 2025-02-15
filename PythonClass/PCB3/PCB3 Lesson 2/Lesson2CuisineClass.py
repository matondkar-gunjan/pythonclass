class Cuisine:
      def __init__(self, name, origin, available):
            self.name = name
            self.origin = origin
            self.available = available
      def describe(self):
            print("Cuisine Name:", self.name)
            print("Origin:", self.origin)
      def check_availability(self):
            if self.available:
                  print(self.name, "is available")
            else:
                  print(self.name, "is not available")
cuisine1 = Cuisine("Sushi", "Japan", True)
cuisine2 = Cuisine("Tacos", "Mexico", False)

cuisine1.describe()
cuisine1.check_availability()
cuisine2.describe()
cuisine2.check_availability()
