import turtle
t = turtle.Pen()
t.speed(0)
def draw_square_spiral(x, y):
      t.penup()
      t.setpos(x, y)
      t.pendown()
      size = 30
      for i in range(size):
            t.forward(i)
            t.right(91)
turtle.onscreenclick(draw_square_spiral)
