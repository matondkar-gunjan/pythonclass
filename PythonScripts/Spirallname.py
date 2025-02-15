import turtle
t=turtle.Pen()
turtle.bgcolor("black")
color=["red","#FFD700","blue","green"]

#Ask the user's name using turtle's textinput pop up window

your_name=turtle.textinput("Beehong asks ???","What is your name?")

#Draw a spiral of the name on the screen,written 100 times

for x in range(100):
      t.pencolor(color[x%4])
      t.penup()
      t.forward(x*6)
      t.pendown()
      t.write(your_name, font=("Arial", int((x+4)/4),"bold"))
      t.left(96)
