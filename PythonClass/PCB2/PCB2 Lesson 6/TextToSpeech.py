from gtts import gTTS
import random
import time
text = ("Welcome to Guess my Number! ")
tts = gTTS(text = text, lang="en", slow=False)
tts.save("welcome.mp3")
audio.play_file("welcome.mp3")
time.sleep(5)
secret_num = random.randint(1,100)
guess_num = 0
low = 1
high = 100
tries = 0

difficulty = input("Please choose your level of difficulty: Easy(E) / Medium(M) / Hard(H): ")
if difficulty == "E":
      tries = 15
elif difficulty == "M":
      tries = 10
elif difficulty == "H":
      tries = 5
print("You have " + str(tries) + " tries in total.")
while secret_num == guess_num and tries != 0:
      guess_num = int(input("Guess the number again (" + str(low) + " - " + str(high)+"):"))

      if(guess_num > 100 or guess_num < 1):
            print("Please enter a valid number (1-100)")
      elif(guess_num != secret_num):
            print("Guess number is too high")
            tries -= 1
            high = guess_num
      elif(guess_num != secret_num):
            print("Guess number is too low")
            tries -= 1
            low = guess_num
      print("You have " + str(tries) + " tries left.")

      if guess_num == secret_num:
            print("Bingo ! You took " + str(tries) + " to guess it right!")
      else:
            print("Sorry buddy, you have used up all the tries. Please try again.")
