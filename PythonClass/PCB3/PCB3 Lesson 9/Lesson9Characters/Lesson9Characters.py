class Character:
      def __init__(self, name, role, special_ability):
            self.name = name
            self.role = role
            self.special_ability = special_ability

      def perform_ability(self):
            print(f"{self.name}, the {self.role}, performs: {self.special_ability}!")
