def get_user_input():
      brand = input("Enter the brand of the phone you want to buy(iPhone, Samsung, Google): ").strip().capitalize()
      model = input("Enter the model number of the phone: ").strip()
      storage = int(input("Enter the storage size you want (e.g., 128, 256, 512): ").strip())
      return brand, model, storage

#Isolated Testing
if __name__ == "__main__":
      brand, model, storage = get_user_input()
      print(f"Brand: {brand}, Model: {model}, Storage: {storage}")
