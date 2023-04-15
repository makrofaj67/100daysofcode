import turtle
import pad
import ortacizgi
import ball
import scoreboard
import cerceve
import time

ekran = turtle.Screen()
ekran.title("Pong Ping Pung")
ekran.screensize(800, 600)
ekran.bgcolor("green")
ekran.tracer(0)

cizgi = ortacizgi.OrtaCizgi()
blok = pad.Pad(-380)
blok2 = pad.Pad(380)
top = ball.Ball()
skortahtasi1 = scoreboard.ScoreBoard(-100)
skortahtasi2 = scoreboard.ScoreBoard(100)
kalas = cerceve.Cerceve(800, 600)
ekran.update()

ekran.listen()
ekran.onkeypress(blok.up, "w")
ekran.onkeypress(blok.down, "s")
ekran.onkeypress(blok2.up, "Up")
ekran.onkeypress(blok2.down, "Down")

game_is_on = True
while game_is_on:
  ekran.update()
  top.move()
  time.sleep(0.1)

  
ekran.exitonclick()
