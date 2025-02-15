import turtle
t = turtle.Pen()
t.speed(1)
def up():
      turtle.forward(50)
def left():
      turtle.left(90)
def right():
      turtle.right(90)
def change_red():
      turtle.pencolor("red")
def change_orange():
      turtle.pencolor("orange")
def change_yellow():
      turtle.pencolor("yellow")
def change_green():
      turtle.pencolor("green")
def change_blue():
      turtle.pencolor("blue")
def change_purple():
      turtle.pencolor("purple")
def change_black():
      turtle.pencolor("black")
turtle.onkeypress(up,"Up")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.onkeypress(change_red,"r")
turtle.onkeypress(change_orange,"o")
turtle.onkeypress(change_yellow,"y")
turtle.onkeypress(change_green,"g")
turtle.onkeypress(change_blue,"b")
turtle.onkeypress(change_purple,"p")
turtle.onkeypress(change_black,"a")
turtle.listen()
