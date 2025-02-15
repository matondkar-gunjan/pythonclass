import turtle
t=turtle.Pen()
turtle.bgcolor("black")
color=["red","#FFD700","blue","green","orange","purple","white","gray","violet","brown"]

#Ask the user's name using turtle's textinput pop up window

#your_name=turtle.textinput("Beehong asks ???","What is your name?")
sides=int(turtle.numinput("Number of sides","How many sides do you want(1-10)?",4,1,10))

#Draw a spiral of the name on the screen,written 100 times

for x in range(360):
      t.pencolor(color[x%sides])
      t.forward(x*3/sides+x)
      t.left(360/sides+1)
      t.width(x*sides/200)

