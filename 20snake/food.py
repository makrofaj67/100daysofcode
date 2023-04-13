import turtle
import random

class Food(turtle.Turtle):
 
 def __init__(self):
  super().__init__()
  self.shape("circle")
  self.penup()
  self.shapesize(stretch_len=0.5, stretch_wid=0.5)
  self.color("red")
  self.speed("fastest")
  self.kabom()
  
 def kabom(self):
  self.goto(random.randint(-280, 280), random.randint(-280, 280))
