class SuperheroAcademy:
      def __init__(self, name, superpower):
            self.name = name
            self.superpower = superpower
            
      def use_superpower(self): #Instance method
            print(f"{self.name} uses {self.superpower}!")

      @staticmethod
      def charge_superpowers(): #Static method
            print("All superheroes must charge their superpowers before going on a mission!")

#Create superhero instances
hero1 = SuperheroAcademy("Captain America", "Shield")
hero2 = SuperheroAcademy("Ironman", "Fly")

#Calling an instance method
hero1.use_superpower()

#Calling a static method
SuperheroAcademy.charge_superpowers() #No need to create an instance

hero1 = SuperheroAcademy("Captain America", "Shield")
hero2 = SuperheroAcademy("Ironman", "Fly")
hero3 = SuperheroAcademy("Hulk", "Smash")
SuperheroAcademy.charge_superpowers()
