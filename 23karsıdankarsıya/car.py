import turtle
import random

class Car():

 def __init__(self):
  self.allcars = []
  self.hiz = 10
  
 def arabaci(self):
  if random.randint(1, 6) == 1:
   yeniaraba = turtle.Turtle()
   yeniaraba.penup()
   yeniaraba.setposition(-350, random.randint(-200, 200))
   yeniaraba.speed(1)
   yeniaraba.shape("square")
   yeniaraba.shapesize(stretch_wid=1, stretch_len=2)
   self.allcars.append(yeniaraba)

 def arabamove(self):
  for mustafa in self.allcars:
   mustafa.setheading(0)
   mustafa.forward(self.hiz)
   
 def hizart(self):
   self.hiz += 5