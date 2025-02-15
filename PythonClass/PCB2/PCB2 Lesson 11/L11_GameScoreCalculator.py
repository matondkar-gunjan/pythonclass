try:
      scores = [50, 80, 90, 70, 60]
      total = sum(scores)
      count = len(scores)
      average_score = total / count
      print("The average score is", average_score)
      index = 10
      player_score = scores[index]
      print("The score of player at index", index, "is", player_score)
except ZeroDivisionError:
      print("Oops! Division by zero is not allowed.")
except IndexError:
      print("Oops! The index you are trying to access is out of range.")
