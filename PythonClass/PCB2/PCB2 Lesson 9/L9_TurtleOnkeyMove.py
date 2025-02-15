import turtle
t = turtle.Pen()
t.speed(1)
def up():
      turtle.forward(50)
def left():
      turtle.left(90)
def right():
      turtle.right(90)
turtle.onkeypress(up,"Up")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()

