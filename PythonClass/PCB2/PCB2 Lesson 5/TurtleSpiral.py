import random
import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
t.pencolor(random.choice(colors))
size = random.randint(10,40)
for m in range(size):
      t.forward(m*2)
      t.left(91)
