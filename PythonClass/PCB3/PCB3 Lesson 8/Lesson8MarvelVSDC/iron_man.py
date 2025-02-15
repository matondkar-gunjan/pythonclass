from Lesson8Hero import Hero

class IronMan(Hero):
      def __init__(self):
            super().__init__(name = "Iron-Man", power = "Advanced Armor")

      def fight(self):
            print("Iron-Man fights using his armor and repulsor blasts!")
