class Animal:
      def __init__(self, name, age, weight):
            self.name = name
            self.age = age
      def show_age(self):
            print(self.name, self.age)

class Dog(Animal):
      def __init__(self, bark_loudness, name, age, weight):
            super().__init__(name, age, weight)
            self.bark_loudness = bark_loudness

class Cat(Animal):
      def __init__(self, lives_left, name, age, weight):
            super().__init__(name, age, weight)
            self.lives_left = lives_left

dog1 = Dog(45, "Casper", 3, 2)
cat1 = Cat(9, "Kitty", 1, 5)

dog1.show_age()
cat1.show_age()
