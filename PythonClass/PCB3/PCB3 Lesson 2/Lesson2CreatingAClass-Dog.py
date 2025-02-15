class Dog:
      def __init__(self, color, gender, height, weight):
            self.color = color
            self.gender = gender
            self.height = height
            self.weight = weight
      def introduction(self):
            print("My dog is " + self.color + ".")
            print("My Dog is a " + self.gender + ".")
            print("My Dog is " + str(self.height) + " m tall.")
            print("My Dog is " + str(self.weight) + " kg.")
      def canBark(self):
            print("Dogs can bark")
      def canRun(self):
            print("Dogs can run")
      def canSwim(self):
            print("Dogs can swim")
      def canSit(self):
            print("Dogs can sit")
dog1 = Dog("Brown", "Male", 1.5, 35)
dog1.introduction()
dog1.canBark()
dog1.canRun()
dog1.canSwim()
dog1.canSit()
