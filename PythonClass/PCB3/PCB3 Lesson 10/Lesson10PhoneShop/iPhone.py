from Smartphone import Smartphone

class iPhone:
      def __init__(self):
            self.models = [
                  Smartphone("iPhone", "13", 799, 128),
                  Smartphone("iPhone", "13", 899, 256),
                  Smartphone("iPhone", "14", 999, 128),
                  Smartphone("iPhone", "14", 1099, 256),
            ]
      def list_models(self):
            print("Available iPhone models:\n")
            for phone in self.models:
                  print(f"-{phone.info()}")

#Isolated Testing
if __name__ == "__main__":
      iphone = iPhone()
      iphone.list_models()
