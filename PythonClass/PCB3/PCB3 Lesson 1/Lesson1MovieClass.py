class Movie:
      def __init__(self, title, director, duration):
            self.title = title
            self.director = director
            self.duration = duration
movie1 = Movie("Toy Story", "John Lasseter", 81)
movie2 = Movie("Frozen", "Chris Buck and Jennifer Lee", 102)

print(movie1.title)
print(movie2.title)

total_duration = movie1.duration + movie2.duration
print("Total duration:", total_duration, "minutes")
