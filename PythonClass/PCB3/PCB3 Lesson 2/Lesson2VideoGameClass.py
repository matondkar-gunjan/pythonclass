class VideoGame:
      total_games = 0
      
      def __init__(self, title, genre, is_installed):
            self.title = title
            self.genre = genre
            self.is_installed = is_installed
            VideoGame.total_games += 1
      def game_details(self):
            print("Title: " + self.title)
            print("Genre: " + self.genre)
      def check_installation(self):
            if self.is_installed:
                  print(self.title + " is installed.")
            else:
                  print(self.title + " is not installed.")
game1 = VideoGame("Minecraft", "Sandbox", True)
game2 = VideoGame("Roblox", "Adventure", False)
game3 = VideoGame("Brawl Stars", "Action", True)

game1.game_details()
game1.check_installation()
game2.game_details()
game2.check_installation()
game3.game_details()
game3.check_installation()

print("Total number of video games in the collection:", VideoGame.total_games)

