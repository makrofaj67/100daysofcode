import turtle
import scoreboard

class Noob(turtle.Turtle):
 def __init__(self):
  super().__init__()
  self.ht()
  
 def noobyaz(self): 
  self.color("red")
  self.write("NOOB", font=("Courier", 50, "bold"))