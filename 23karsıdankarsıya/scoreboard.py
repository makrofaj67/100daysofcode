import turtle

class ScoreBoard(turtle.Turtle):
 
 def __init__(self):
  super().__init__()
  self.penup()
  self.setposition(-270, 260)
  self.ht()
  self.bolum = 0
  self.skorupdate()
  
 def skorart(self):
  self.bolum += 1
  
 def skorupdate(self):
  self.clear()
  self.write(f"Bölüm: {self.bolum}", font=("Courier", 18, "bold"))