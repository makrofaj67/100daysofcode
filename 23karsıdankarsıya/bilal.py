import turtle

class Bilal(turtle.Turtle):
 def __init__(self):
  super().__init__()
  self.color("green")
  self.penup()
  self.setposition(0, -280)
  self.shape("turtle")
  self.setheading(90)
  
 def moveup(self):
  newy = self.ycor() + 10
  self.sety(newy)