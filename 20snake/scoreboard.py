import turtle
import os

class Scoreboard(turtle.Turtle):
 def __init__(self):
  super().__init__()
  self.penup()
  self.goto(0, 260)
  self.color("white")
  self.ht()
  self.score = 0
  with open("20snake/highscore.txt", "r") as dosya:
   self.highscore = int(dosya.read())  
  
 def puanart(self):
  self.score += 1 
 
 def skortahtasiguncelle(self):
  self.write(f"score: {self.score}, highscore: {self.highscore}")
  
 def yuksekskorguncelle(self):
  if self.score > self.highscore:
   self.highscore = self.score
 
 def resetscore(self):
  self.score = 0
   
 def highscoreyaz(self):
  with open("20snake/highscore.txt", "w") as dosya:
   dosya.write(f"{self.highscore}")
 
 def highscoreoku(self):
  with open("20snake/highscore.txt", "r") as dosya:
   self.highscore = int(dosya.read())