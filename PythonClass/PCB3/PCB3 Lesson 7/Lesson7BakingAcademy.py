class BakingAcademy:
      #Class attribute to count number of bakers
      baker_count = 0

      def __init__(self, name, specialty):
            self.name = name
            self.specialty = specialty
            BakingAcademy.baker_count += 1 #Increment the baker count each time a new baker is created

      def show_specialty(self):
            print(f"{self.name} specializes in {self.specialty}!")

      @staticmethod
      def display_baker_count():
            #Accessing the class attribute using the class name
            print(f"Number of bakers: {BakingAcademy.baker_count}")

#Creating baker objects
baker1 = BakingAcademy("Alice", "Cakes")
baker2 = BakingAcademy("Bob", "Cookies")

#Calling instance methods
baker1.show_specialty()
baker2.show_specialty()

#Calling the static method
BakingAcademy.display_baker_count()
