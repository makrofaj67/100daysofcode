import turtle
BASLANGIC_KONUMU = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
 
 def __init__(self):
  self.parcalar = []
  self.sineykyap()
  
 def sineykyap(self):
  for pozisyon in BASLANGIC_KONUMU:
   yenikisim = turtle.Turtle(shape="square")
   yenikisim.color("white")
   yenikisim.penup()
   yenikisim.goto(pozisyon)
   self.parcalar.append(yenikisim)
   
 def up(self):
  self.parcalar[0].setheading(90)
 def down(self):
  self.parcalar[0].setheading(270)
 def left(self):
  self.parcalar[0].setheading(180)
 def right(self):
  self.parcalar[0].setheading(0)
   
 def ileri(self):
  for i in range(len(self.parcalar) - 1, 0, -1):
   yenix = self.parcalar[i-1].xcor()
   yeniy = self.parcalar[i-1].ycor()
   self.parcalar[i].goto(yenix, yeniy)
  self.parcalar[0].forward(MOVE_DISTANCE)
  
 def kisimekle(self):
  yeni_kisim = self.parcalar[-1].clone()
  self.parcalar.append(yeni_kisim)
