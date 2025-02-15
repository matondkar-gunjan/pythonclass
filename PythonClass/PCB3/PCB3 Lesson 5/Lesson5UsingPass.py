class Pet:
      def __init__(self, name):
            self.name = name

      def make_sound(self):
            pass #This will be overidden in subclasses

class Cat(Pet):
      def __init__(self):
            super().__init__(name = "Cat")

      def make_sound(self):
            print(f"{self.name} says Meow!")

class Dog(Pet):
      def __init__(self):
            super().__init__(name = "Dog")

      def make_sound(self):
            print(f"{self.name} says Woof!")

cat = Cat()
dog = Dog()

cat.make_sound()
dog.make_sound()
