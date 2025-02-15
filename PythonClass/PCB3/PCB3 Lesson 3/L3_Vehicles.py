class Vehicle:
      def __init__(self, color, number_of_wheels):
            self.color = color
            self.number_of_wheels = number_of_wheels

      def get_details(self):
            return "Color: " + self.color + ", Number of wheels: " + str(self.number_of_wheels)

class Car(Vehicle):

      def __init__(self, license_plate, make, color, number_of_wheels):
            super().__init__(color, number_of_wheels)
            self.license_plate = license_plate
            self.make = make

      def get_details(self):
            base_details = super().get_details()
            return base_details + ", License plate: " + self.license_plate + ", Brand: " + self.make
      
car1 = Car("SFX 9870 E", "Tesla", "Blue", 4)
print(car1.get_details())


