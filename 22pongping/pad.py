import turtle

class Pad(turtle.Turtle):
 
 def __init__(self, x):
  super().__init__()
  self.ht()
  self.penup()
  self.shape("square")
  self.color("white")
  self.shapesize(stretch_wid=3, stretch_len=0.5)
  self.speed("fastest")
  self.goto(x, 0)
  self.st()
  
 def up(self):
  self.sety(self.ycor() + 20)
 def down(self):
  self.sety(self.ycor() - 20)
  