class Shape:
      def __init__(self, color):
            self.color = color

      def get_area(self):
            return "Area" 

      def get_details(self):
            return "Color: " + self.color

class Rectangle(Shape):

      def __init__(self, color, width, height):
            super().__init__(color)
            self.width = width
            self.height = height

      def get_area(self):
            return self.width * self.height

      def get_details(self):
            base_details = super().get_details()
            return "Rectangle - " + base_details
class Triangle(Shape):
      def __init__(self, color, base, height):
            super().__init__(color)
            self.base = base
            self.height = height

      def get_area(self):
            return self.base * self.height * 0.5
      
      def get_details(self):
            base_details = super().get_details()
            return "Triangle - " + base_details
      
      
triangle1 = Triangle("Green", 10, 15)
rectangle1 = Rectangle("Yellow", 20, 30)

print(triangle1.get_details(), ", Area: ", triangle1.get_area())
print(rectangle1.get_details(), ", Area: ", rectangle1.get_area())


