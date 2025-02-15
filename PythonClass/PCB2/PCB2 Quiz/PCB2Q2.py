movieList = []
num_movies  = int(input("How many movies do you want to store?: "))
while len(movieList) < num_movies:
      title_of_movie = input("Enter the title of the movie: ")
      movieList.append(title_of_movie)
print("You have entered the following movies: ", movieList) 
for x in movieList:
      print(x)

