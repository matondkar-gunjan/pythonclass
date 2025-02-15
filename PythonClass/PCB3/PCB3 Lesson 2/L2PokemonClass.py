class Pokemon:
      center_limit = 3
      current_pokemon = []
      
      def __init__(self, name, type, is_healthy):
            self.name = name
            self.type = type
            self.is_healthy = is_healthy
            
      def pokemon_type(self):
            print("Pokemon Type: " + self.type)
            
      def health_condition(self):
            if self.is_healthy:
                  print(self.type + " is healthy")
            else:
                  print(self.type + " needs healing")

      def admit_to_center(self):
            if not self.is_healthy:
                  if len(Pokemon.current_pokemon) < self.center_limit:
                        Pokemon.current_pokemon.append(self)
                        print(self.name + " has been admitted to the health center")
                  else:
                              print("The health center is full. Cannot admit " + self.name + ".")
            else:
                  print(self.name + " does not need to be admitted to the health center")

      def release_from_center(self):
            if self in Pokemon.current_pokemon:
                  if self.is_healthy:
                        Pokemon.current_pokemon.remove(self)
                        print(self.name + " has been released from the health center.")
                  else:
                        print(self.name + " cannot be released until it is healed.")
            else:
                  print(self.name + " is not in the health center.")
pikachu = Pokemon("Pikachu", "Electric", False)
bulbasaur = Pokemon("Bulbasaur", "Grass", False)
charmander = Pokemon("Charmander", "Fire", False)
squirtle = Pokemon("Squirtle", "Water", False)

pikachu.pokemon_type()
pikachu.health_condition()

pikachu.admit_to_center()
bulbasaur.admit_to_center()
charmander.admit_to_center()
squirtle.admit_to_center()

pikachu.is_healthy = True
pikachu.release_from_center()
squirtle.admit_to_center()
