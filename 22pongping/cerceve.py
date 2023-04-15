import turtle

class Cerceve(turtle.Turtle):
 def __init__(self,x ,y):
  super().__init__()
  self.penup()
  self.goto(x/2, y/2)
  self.pensize(3)
  self.color('black') 
  self.right(90)
  self.pendown()
  self.forward(y)
  self.right(90)
  self.forward(x)
  self.right(90)
  self.forward(y)
  self.right(90)
  self.forward(x)
  self.hideturtle()
  