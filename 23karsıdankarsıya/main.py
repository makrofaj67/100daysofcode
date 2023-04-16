import turtle
import car
import time
import bilal
import scoreboard
import noob

ekran = turtle.Screen()
ekran.listen()
ekran.bgcolor("white")
ekran.setup(width=600, height=600)
ekran.tracer(0)

kalem = noob.Noob()
kurba = bilal.Bilal()
skortahtasi = scoreboard.ScoreBoard()
ekran.update()

ekran.onkeypress(kurba.moveup, "w")

araba = car.Car()

game_is_on = True
while game_is_on:
 
 araba.arabaci()
 araba.arabamove()
 time.sleep(0.1)
 
 for kutu in araba.allcars:
  if kutu.distance(kurba) < 20:
   game_is_on = False
   kalem.noobyaz()  
   
 if kurba.ycor() > 250:
   kurba.setposition(0, -280)
   araba.hizart()
   skortahtasi.skorart()
   skortahtasi.skorupdate()
  
 ekran.update()
 
ekran.exitonclick()