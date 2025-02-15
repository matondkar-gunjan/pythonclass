from Fireninja import FireNinja
import random
import time

def dodge_fireball(ninja):
      print(f"{ninja.name} is about to dodge an incoming fireball")
      time.sleep(1)

      #Random chance of fireball hitting or missing
      if random.random() > 0.5:
            print("Oh no! The fireball hit!")
            ninja.receive_damage(20)
      else:
            print("Great! You dodged the fireball successfully!")

      ninja.show_status()


def main():
      player = FireNinja(name="FireNinja Player", chakra=50, health=100, attack_power=70, healing_ability=30, ignite_chance=0.2)
      player.show_status

      for i in range(3):
            print(f"Attempt {i + 1} to dodge a fireball:")
            dodge_fireball(player)

            if player.health <= 0:
                  print("The ninja has been defeated by the fireball!")
                  break
            
      if player.health != 0:
            print("Congratulations! The ninja survived all the fireballs!")

main()
