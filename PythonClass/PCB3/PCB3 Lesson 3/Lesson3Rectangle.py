class Rectangle:
      def __init__(self, length, width):
            self.length = length
            self.width = width
      def perimeter(self):
            return 2 * (self.length + self.width)
      def area(self):
            return self.length * self.width
      def display(self):
            print("The length of the rectangle is: ", self.length)
            print("The width of the rectange is: ", self.width)
            print("The perimeter of the rectange is: ", self.perimeter())
            print("The area of the rectange is: ", self.area())

myRectangle = Rectangle(10, 20)
myRectangle.display()
