import turtle
import time
import snake
import food
import scoreboard
import os

ekran = turtle.Screen()
ekran.setup(600, 600)
ekran.bgcolor("black")
ekran.title("yılan oyunu")
ekran.tracer(0)

my_snake = snake.Snake()
yemek = food.Food()

if not os.path.exists("20snake/highscore.txt"):
 with open("20snake/highscore.txt", "w") as dosya:
  dosya.write("0")
 
skor = scoreboard.Scoreboard()
skor.highscoreoku()
skor.skortahtasiguncelle()

ekran.listen()

ekran.onkeypress(my_snake.up, "w")
ekran.onkeypress(my_snake.down, "s")  
ekran.onkeypress(my_snake.left, "a")
ekran.onkeypress(my_snake.right, "d")

game_is_on = True
while game_is_on:
 ekran.update()
 time.sleep(0.1)
 my_snake.ileri()

 if my_snake.parcalar[0].distance(yemek) < 15:
  skor.clear()
  skor.puanart()
  skor.yuksekskorguncelle()
  skor.skortahtasiguncelle()
  skor.highscoreyaz()  
  yemek.kabom()  
  my_snake.kisimekle()  
 
 if my_snake.parcalar[0].xcor() > 280 or my_snake.parcalar[0].xcor() < -280 or my_snake.parcalar[0].ycor() > 280 or my_snake.parcalar[0].ycor() < -280:
  skor.clear()
  skor.resetscore()
  skor.skortahtasiguncelle()  
  my_snake.sineykreset()  
  
 for kisim in my_snake.parcalar[1:]:
  if my_snake.parcalar[0].distance(kisim) < 10:
   skor.clear()
   skor.resetscore()
   skor.skortahtasiguncelle()   
   my_snake.sineykreset()
  
ekran.exitonclick()