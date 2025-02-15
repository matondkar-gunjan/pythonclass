from Lesson9Sports import Sport

class Volleyball(Sport):
      def __init__(self):
            super().__init__(name_of_sports = "Volleyball", number_of_players = 6)

      def play(self):
            print("Playing volleyball: The game starts with a ball smack!")
