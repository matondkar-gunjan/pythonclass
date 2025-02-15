from spider_man import SpiderMan
from batman import Batman

def battle(hero1, hero2):
      print(f"{hero1.name} vs {hero2.name}! Let the battle begin!")
      hero1.introduce()
      hero2.introduce()
      while hero1.health > 0 and hero2.health > 0:

            hero1.attack(hero2)

            if hero2.health <= 0:
                  print(f"{hero2.name} has been defeated!")
                  break
            
            hero2.attack(hero1)
            
            if hero1.health <= 0:
                  print(f"{hero1.name} has been defeated!")
                  break
            
      print("Battle Over!")

def main():
      spiderman = SpiderMan()
      batman = Batman()
      battle(spiderman, batman)

main()
            
