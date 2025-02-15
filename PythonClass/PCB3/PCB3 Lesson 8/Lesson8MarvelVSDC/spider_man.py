from Lesson8Hero import Hero

class SpiderMan(Hero):
      def __init__(self):
            super().__init__(name = "Spider-Man", power = "Super Agility")
            self.health = 100
      
      def fight(self):
            print("Spider-Man fights using his agility and web-slinging!")

      def attack(self, opponent):
            damage = 15
            print(f"Spider-Man attacks {opponent.name} causing {damage} damage!")
            opponent.health -= damage

