import turtle

class ScoreBoard(turtle.Turtle):
 def __init__(self, x):
  super().__init__()
  self.ht()
  self.penup()
  self.color("white")
  self.goto(x, 300)  
  self.score = 0
  self.update_skor()
  
 def update_skor(self):
  self.write(f"{self.score}", align="center", font=("Times New Roman", 24, "bold"))
  
 def skorart(self):
  self.score += 1
  self.clear()
  self.update_skor()