import turtle
colors=["white","blue","black","green","red"]
for x in range(5):
      turtle.bgcolor(colors[x%5])
      t=turtle.Pen()
      for y in range(10):
            t.pencolor(colors[y%5])
            t.circle(y)
            t.left(91)
            
