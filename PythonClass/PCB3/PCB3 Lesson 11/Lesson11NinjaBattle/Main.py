from CreateNinja import create_ninja
from Fireninja import FireNinja
from Waterninja import WaterNinja
import random

def battle(ninja, enemy_ninja):

      can_defend = False

      while True:
            ninja.show_status()
            enemy_ninja.show_status()

            print("What do you want to do?")
            print("1. Attack")
            print("2. Heal")
            print("3. Defend")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                  damage = ninja.attack()
                  if damage > 0:
                        enemy_ninja.receive_damage(damage)

                  #Ensure can defend is set to False when attacking
                  can_defend = False

            elif choice == 2:
                  ninja.heal()
                  #Ensure can defend is set to False when attacking
                  can_defend = False

            elif choice == 3:
                  can_defend = ninja.defend()

            elif choice == 4:
                  print("Battle session ends.")
                  break


            if enemy_ninja.health <= 0:
                  print("Congratulations! You have defeated the enemy ninjs.")
                  break
            print("\n")
            print("Enemy ninja attacks!")
            damage = enemy_ninja.attack()

            if can_defend == True:
                  ninja.receive_damage(damage, defending = True)
            else:
                  ninja.receive_damage(damage)

            ninja.cooldown_tick()               
            enemy_ninja.cooldown_tick()

            if ninja.chakra <= 0:
                  print(f"Oh no! {ninja.name} has run out of chakra and can't continue fighting.")
                  break
            
            if ninja.health <= 0:
                  print(f"Oh no! Try again!")
                  break

def main():
      ninja, enemy_type = create_ninja()
      if enemy_type == 2:
            enemy_ninja = WaterNinja("Enemy Water Ninja", chakra=80, health=120, attack_power=70, healing_ability=30, water_shield=0.3)
      else:
            enemy_ninja = FireNinja("Enemy Fire Ninja", chakra=80, health=120, attack_power=70, healing_ability=30, ignite_chance=0.2)

      #Start the battle
      battle(ninja, enemy_ninja)

main()
