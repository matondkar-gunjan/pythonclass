class Vehicle:
      def __init__(self, color):
            self.color = color

      def get_details(self):
            return "Color: " + self.color

class Aeroplane(Vehicle):

      def __init__(self, home_airport, airline, color):
            super().__init__(color)
            self.home_airport = home_airport
            self.airline = airline

      def get_details(self):
            return "I am a " + self.color + " plane and I fly from " + self.home_airport

aeroplane1 = Aeroplane("Singapore Airport", "Singapore Airlines", "white")
print(aeroplane1.get_details())


