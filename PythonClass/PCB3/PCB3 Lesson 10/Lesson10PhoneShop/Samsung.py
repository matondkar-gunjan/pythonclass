from Smartphone import Smartphone

class Samsung:
      def __init__(self):
            self.models = [
                  Smartphone("Samsung", "Galaxy S23", 799, 128),
                  Smartphone("Samsung", "Galaxy S23+", 999, 256),
                  Smartphone("Samsung", "Galaxy S23 Ultra", 1199, 512),
            ]
      def list_models(self):
            print("Available Samsung models:\n")
            for phone in self.models:
                  print(f"-{phone.info()}")

#Isolated Testing
if __name__ == "__main__":
      samsung = Samsung()
      samsung.list_models()
