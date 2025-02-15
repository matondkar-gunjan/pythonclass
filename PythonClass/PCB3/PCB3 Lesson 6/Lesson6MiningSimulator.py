import random
class MiningTools:
      money = 100
      ores = 0
      workers_created = 0

      def __init__(self, mining_power, cost):
            self.mining_power = mining_power
            self.cost = cost
            MiningTools.workers_created += 1

      def mine_ore(self):
            MiningTools.ore += self.mining_power

      def show_workers_created(self):
            print("Total mining workers created:", MiningTools.workers_created)

class MiningExpert(MiningTools):
      def __init__(self, mining_power = 10, cost = 20):
            super().__init__(mining_power, cost)

class MiningDrill(MiningTools):

      def __init__(self, mining_power = 20, cost = 50, drilling_power = 1.1):
            super().__init__(mining_power, cost)
            self.drilling_power = drilling_power

      def mine_ore(self):
            if random.random() < 0.3:
                  effective_mining_power = self.mining_power * self.drilling_power
            else:
                  effective_mining_power = self.mining_power

            return effective_mining_power

class MiningBulldozer(MiningTools):
      def __init__(self, mining_power = 30, cost = 100, drilling_power = 1.5):
            super().__init__(mining_power, cost)
            self.drilling_power = drilling_power

      def mine_ore(self):
            if random.random() < 0.5:
                  effective_mining_power = self.mining_power * self.drilling_power
            else:
                  effective_mining_power = self.mining_power

            return effective_mining_power


def main():
      mining_experts = []
      mining_drills = []
      mining_bulldozers = []

      while True:
            print("\n=== Mining Simulator Menu ===")
            print("Press Enter to continue mining")
            print("Enter 1 to view total mining power, number of ores, and money")
            print("Enter 2 to view the total number of different mining equipment")
            print("Enter 3 to change ores into money")
            print("Enter 4 to purchase mining equipment")
            print("Enter Q to quit the game")

            choice = input("Choose an option: ")
                  
            if choice == "":
                  #Continue mining
                  total_ores_mined = 0 #Initialize a counter for ores mined

                  #Mine ores using each expert
                  for expert in mining_experts:
                        expert.mine_ore()

                  #Mine ores using each drill
                  for drill in mining_drills:
                        total_ores_mined += drill.mine_ore()

                  #Mine ores using each bulldozer
                  for bulldozer in mining_bulldozers:
                        total_ores_mined += bulldozer.mine_ore()

                  #Update total ores with mined amount
                  MiningTools.ores += total_ores_mined
                  print("Mined ores. Total ores:", MiningTools.ores)


            elif choice == "1":
                  #Initialize total mining power
                  total_mining_power = 0

                  #Calculate mining power from Mining Experts
                  for expert in mining_experts:
                        total_mining_power += expert.mining_power

                  #Calculate mining power from Mining Drills
                  for expert in mining_drills:
                        total_mining_power += drill.mining_power * drill.drilling_power

                  #Calculate mining power from Mining Bulldozers
                  for expert in mining_bulldozers:
                        total_mining_power += bulldozer.mining_power * bulldozer.drilling_power

                  #Display the results
                  print("Total mining power:", total_mining_power)
                  print("Total ores:", MiningTools.ores)
                  print("Total money:", MiningTools.money)

            elif choice == "2":
                  #View the total number of different mining equipment
                  if mining_experts: #Return true if list not empty
                        mining_experts[0].show_workers_created()
                  elif mining_drills:
                        mining_drills[0].show_drills_created()
                  elif mining_bulldozers:
                        mining_bulldozers[0].show_bulldozers_created()
                  else:
                        print("No workers created")

                  print("Mining experts:", len(mining_experts))
                  print("Mining drills:", len(mining_drills))
                  print("Mining bulldozers:", len(mining_bulldozers))

            elif choice == "3":
                  #Change ores into money
                  MiningTools.money += MiningTools.ores
                  print("Converted", MiningTools.ores, "ores into money. Total money:", MiningTools.money)
                  MiningTools.Ores = 0

            elif choice == "4":
                  #Purchase mining equipment
                  print("\n=== Purchase Mining Equipment ===")
                  print("1. Mining Expert ($20)")
                  print("2. Mining Drill ($50)")
                  print("3. Mining Bulldozer ($100)")
                  equipment_choice = input("Choose equipment to purchase: ")

                  if equipment_choice == "1":
                        if MiningTools.money >= 20:
                              mining_experts.append(MiningExpert())
                              MiningTools.money -= 20
                              print("Purchased a Mining Expert")
                        else:
                              print("Not enough money to purchase a Mining Expert")

                  elif equipment_choice == "2":
                        if MiningTools.money >= 50:
                              mining_drills.append(MiningDrill())
                              MiningTools.money -= 50
                              print("Purchased a Mining Drill")
                        else:
                              print("Not enough money to purchase a Mining Drill")

                  elif equipment_choice == "3":
                        if MiningTools.money >= 100:
                              mining_bulldozers.append(MiningBulldozer())
                              MiningTools.money -= 100
                              print("Purchased a Mining Bulldozer")
                        else:
                              print("Not enough money to purchase a Mining Bulldozer")


                  else:
                        print("Invalid option. Please try again.")

            elif choice == "Q":
                  #Quit the game
                  print("Quitting the game. Goodbye!")
                  break

            else:
                  print("Invalid option. Please try again.")

##Run the game
main()

            
