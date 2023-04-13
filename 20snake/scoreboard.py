import turtle

class Scoreboard(turtle.Turtle):
 def __init__(self):
  super().__init__()
  self.penup()
  self.goto(0, 260)
  self.color("white")
  self.ht()
  self.write("Score: 0", align="center", font=("Courier", 24, "normal"))
  
