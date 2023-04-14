import turtle
import pad
import ortacizgi

ekran = turtle.Screen()
ekran.title("Pong Ping Pung")
ekran.screensize(600, 600)
ekran.bgcolor("green")
ekran.tracer(0)

cizgi = ortacizgi.OrtaCizgi()
blok = pad.Pad(-200)
blok2 = pad.Pad(200)
ekran.update()

game_is_on = True
while game_is_on:
 ekran.update()
 ekran.listen()
 ekran.onkeypress(blok.up, "w")
 ekran.onkeypress(blok.down, "s")
 ekran.onkeypress(blok2.up, "Up")
 ekran.onkeypress(blok2.down, "Down")

ekran.exitonclick()

