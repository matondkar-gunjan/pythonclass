from Lesson8Hero import Hero

class Batman(Hero):
      def __init__(self):
            super().__init__(name = "Batman", power = "Martial Arts and Gadgets")
            self.health = 100

      def fight(self):
            print("Batman fights using his martial arts and gadgets!")

      def attack(self, opponent):
            damage = 40
            print(f"Batman attacks {opponent.name} causing {damage} damage!")
            opponent.health -= damage
