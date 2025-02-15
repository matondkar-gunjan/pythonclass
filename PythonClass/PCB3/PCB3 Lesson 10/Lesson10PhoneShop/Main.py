#Main.py
from Smartphone import Smartphone
from iPhone import iPhone
from Samsung import Samsung
from Google import Google
from UserInput import get_user_input

def main():
      print("Welcome to the Smartphone Store!")
      print("Available Phones:")

      iphone = iPhone()
      samsung = Samsung()
      google = Google()
      iphone.list_models()
      samsung.list_models()
      google.list_models()

      all_models = iphone.models + samsung.models + google.models

      current_brand, current_model, current_storage = get_user_input()

      selected_phone = None
      for phone in all_models:
            if phone.brand.lower() == current_brand.lower() and phone.model.lower() == current_model.lower() and phone.storage == current_storage:
                  selected_phone = phone
                  break
      if selected_phone:
            print(f"You have selected {selected_phone.info()}.")
            print(f"Your total is: ${selected_phone.price}. Thank you for shopping with us!")
      else:
            print("Sorry, the phone model and storage size you selected are not available")

main()            
