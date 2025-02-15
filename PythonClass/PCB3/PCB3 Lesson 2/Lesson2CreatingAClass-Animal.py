class Animal:
      def __init__(self, species, gender, weight, color):
            self.species = species
            self.gender = gender
            self.weight = weight
            self.color = color
      def can_fly(self):
            if self.species != "Birds":
                  print(self.species + " cannot fly")
            else:
                  print(self.species + " can fly")
birds = Animal("Birds", "Male", 1, "Blue")
birds.can_fly()
