from Lesson9Characters import Character

class Healer(Character):
      def __init__(self):
            super().__init__(name = "Lightbringer", role = "Healer", special_ability = "Heal Alies")

      def special_attack(self):
            print(f"{self.name} channels divine light to restore health to all allies")

if __name__ == "__main__":
      healer1 = Healer()
      healer1.perform_ability()
      healer1.special_attack()
