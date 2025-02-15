from Lesson9Sports import Sport

class Badminton(Sport):
      def __init__(self):
            super().__init__(name_of_sports = "Badminton", number_of_players = 2)

      def play(self):
            print("Playing badminton: The game starts with a serve!")
