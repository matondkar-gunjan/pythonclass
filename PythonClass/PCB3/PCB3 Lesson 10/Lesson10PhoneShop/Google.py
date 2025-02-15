from Smartphone import Smartphone

class Google:
      def __init__(self):
            self.models = [
                  Smartphone("Google", "Pixel 7", 599, 128),
                  Smartphone("Google", "Pixel 7 Pro", 899, 256),
            ]
      def list_models(self):
            print("Available Google models:\n")
            for phone in self.models:
                  print(f"-{phone.info()}")

#Isolated Testing
if __name__ == "__main__":
      google = Google()
      google.list_models()
