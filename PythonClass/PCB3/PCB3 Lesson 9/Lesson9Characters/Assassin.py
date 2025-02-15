from Lesson9Characters import Character

class Assassin(Character):
      def __init__(self):
            super().__init__(name = "Shadowblade", role = "Assassin", special_ability = "Stealth Attack")

      def special_attack(self):
            print(f"{self.name} vanishes into the shadows and delivers a deadly critical hit!")

if __name__ == "__main__":
      assassin1 = Assassin()
      assassin1.perform_ability()
      assassin1.special_attack()
