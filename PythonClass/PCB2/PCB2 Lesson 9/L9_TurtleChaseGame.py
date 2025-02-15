import turtle
catcher = turtle.Turtle()
runner = turtle.Turtle()
catcher.color("red")
catcher.shape("turtle")
catcher.penup()
catcher.goto(-100, 0)

runner.color("blue")
runner.shape("turtle")
runner.penup()
runner.goto(100, 0)

def move_catcher_up():
      y = catcher.ycor()
      catcher.sety(y + 20)
def move_catcher_down():
      y = catcher.ycor()
      catcher.sety(y - 20)
def move_catcher_left():
      x = catcher.xcor()
      catcher.setx(x - 20)
def move_catcher_right():
      x = catcher.xcor()
      catcher.setx(x + 20)

def move_runner_up():
       y = runner.ycor()
       runner.sety(y + 20)
def move_runner_down():
      y = runner.ycor()
      runner.sety(y - 20)
def move_runner_left():
      x = runner.xcor()
      runner.setx(x - 20)
def move_runner_right():
      x = runner.xcor()
      runner.setx(x + 20)

turtle.listen()
turtle.onkeypress(move_catcher_up, "w")
turtle.onkeypress(move_catcher_down, "s")
turtle.onkeypress(move_catcher_left, "a")
turtle.onkeypress(move_catcher_right, "d")

turtle.onkeypress(move_runner_up, "Up")
turtle.onkeypress(move_runner_down, "Down")
turtle.onkeypress(move_runner_left, "Left")
turtle.onkeypress(move_runner_right, "Right")

def check_collision():
      if catcher.distance(runner) < 20:
            print("Player 2 loses!")
            turtle.bye()
      turtle.ontimer(check_collision, 100)
check_collision()
