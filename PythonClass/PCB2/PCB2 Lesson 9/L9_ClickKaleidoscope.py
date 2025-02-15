import random
import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "gray",]
def draw_kaleidoscope(x, y):
      t.color(random.choice(colors))
      size = random.randint(10, 40)
      draw_spiral(x, y, size)
      draw_spiral(-x, y, size)
      draw_spiral(-x, -y, size)
      draw_spiral(x, -y, size)
def draw_spiral(x, y, size):
      t.penup()
      t.setpos(x, y)
      t.pendown()
      for i in range(size):
            t.forward(i*2)
            t.right(92)
turtle.onscreenclick(draw_kaleidoscope)
