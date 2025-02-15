import turtle
t=turtle.Pen()
turtle.bgcolor("black")
sides=eval(input("choose a side number between 1-6 \n"))
colors=["red","yellow","blue","orange","green","purple"]
for x in range(360):
      t.pencolor(colors[x%sides])
      t.forward(x * 3/sides+x)
      t.left(360/sides+1)
      t.width(x*sides/200)

      
