class Smartphone:
      def __init__(self, brand, model, price, storage):
            self.brand = brand
            self.model = model
            self.price = price
            self.storage = storage

      def info(self):
            return f"{self.brand} {self.model} - ${self.price} ({self.storage}GB)"
if __name__ == "__main__":
      test_phone = info("TestBrand", "TestModel", 999, 256)
      print(test_phone.info)
