from Lesson9Characters import Character

class Marksman(Character):
      def __init__(self):
            super().__init__(name = "Deadeye", role = "Marksman", special_ability = "Precision Shot")

      def special_attack(self):
            print(f"{self.name} takes aim and fires a powerful shot that pierces through the enemies")

if __name__ == "__main__":
      marksman1 = Marksman()
      marksman1.perform_ability()
      marksman1.special_attack()
