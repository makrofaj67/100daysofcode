import random
import turtle

class Ball(turtle.Turtle):

 def __init__(self):
  super().__init__()
  self.penup()
  self.shape("square")
  self.shapesize(stretch_wid=0.5, stretch_len=0.5)
  self.color("white")  

 def move(self):
  new_x = self.xcor() + 1
  new_y = self.ycor() + 1
  self.goto(self.xcor() + new_x, self.ycor() + new_y)
  