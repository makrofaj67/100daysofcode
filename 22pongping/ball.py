import random
import turtle

class Ball(turtle.Turtle):

 def __init__(self):
  super().__init__()
  self.penup()
  self.shape("circle")
  self.shapesize(stretch_wid=0.5, stretch_len=0.5)
  self.color("white")
  self.xmove = 10
  self.ymove = 10

 def move(self):
  new_x = self.xcor() + self.xmove
  new_y = self.ycor() + self.ymove
  self.goto(new_x, new_y)
  
 def bouncekenar(self):
  self.ymove *= -1

 def bouncepad(self):
  self.xmove *= -1
  
 def restet(self):
  self.setposition(0,0)
  self.bouncepad()
 