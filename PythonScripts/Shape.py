import turtle
t=turtle.Pen()
def square():
      t.forward(10)
      t.left(90)
colors = ["blue","red","orange","black"]
for x in range(12):
      t.pencolor(colors[x%4])
      if x < 1:
            for y in range(5):
                  square()
            t.right(180)
      else:
            for y in range(6):
                  square()
            t.left(180)
'''
t.pencolor("red")
t.right(180)
for x in range(6):
      square()
t.pencolor("orange")
t.left(180)
for x in range(5):
      t.forward(100)
      t.left(90)
'''
      
      
