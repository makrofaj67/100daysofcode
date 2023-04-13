import turtle

class Scoreboard(turtle.Turtle):
 def __init__(self):
  super().__init__()
  self.penup()
  self.goto(0, 260)
  self.color("white")
  self.ht()
  self.score = 0
  self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
  
 def puanart(self):
  self.score += 1
  self.clear()
  self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
