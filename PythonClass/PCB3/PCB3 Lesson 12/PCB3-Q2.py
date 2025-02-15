class BakeryShop:
      def __init__(self, name, baking_time):
            self.name = name
            self.baking_time = baking_time

      def show_baking_details(self):
            return "Name: " + self.name + ", Baking time: " + str(self.baking_time) + " minutes"
          
class Bread(BakeryShop):
            def __init__(self, name, baking_time,crustiness_level):
                  super().__init__(name, baking_time)
                  self.crustiness_level = crustiness_level

            def show_baking_details(self):
                  base_details = super().show_baking_details()
                  return base_details + ", Crustiness level: " + str(self.crustiness_level) 
                  
            

class Pastry(BakeryShop):
      def __init__(self, name, baking_time,sweetness_level):
            super().__init__(name, baking_time)
            self.sweetness_level = sweetness_level

      def show_baking_details(self):
            base_details = super().show_baking_details()
            return base_details + ", Sweetness level: " + str(self.sweetness_level) 
                  


bread1 = Bread("Sourdough", 40, 8)
pastry1 = Pastry("Croissant", 25, 6)

print(bread1.show_baking_details())
print("\n")
print(pastry1.show_baking_details())








      
