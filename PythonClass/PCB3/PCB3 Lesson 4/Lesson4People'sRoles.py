class Person:
      def __init__(self, name):
            self.name = name
            
      def role(self):
            print("I'm", self.name, "and I have many roles.")

class Sibling(Person):
      def role(self):
            print("I'm", self.name, "and I am a caring sibling.")

class Student(Person):
      def role(self):
            print("I'm", self.name, "and I am a hardworking student.")

class Friend(Person):
      def role(self):
            print("I'm", self.name, "and I am a loyal friend.")

john = Sibling("John")
lisa = Student("Lisa")
mike = Friend("Mike")

for person in (john, lisa, mike):
      person.role()
