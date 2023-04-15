import turtle

class OrtaCizgi(turtle.Turtle):
 
 def __init__(self):
  super().__init__()
  self.ht()
  self.penup()
  self.speed("fastest")
  self.goto(0,-400)
  self.setheading(90)
  self.pensize(2)
  self.pencolor("white")
  for i in range(200):
   self.pendown()
   self.forward(10)
   self.penup()
   self.forward(10)