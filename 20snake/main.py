import turtle
import time
import snake
ekran = turtle.Screen()
ekran.setup(600, 600)
ekran.bgcolor("black")
ekran.title("yılan oyunu")
ekran.tracer(0)

my_snake = snake.Snake()
yemek = food.Food()
skor = scoreboard.Scoreboard()

ekran.listen()
ekran.onkey(my_snake.up, "Up")
ekran.onkey(my_snake.down, "Down")
ekran.onkey(my_snake.left, "Left")
ekran.onkey(my_snake.right, "Right") ##kuzenim ekran.listen yazmış hepsine

game_is_on = True
while game_is_on:
 ekran.update()
 time.sleep(0.1)
 my_snake.ileri()
 
 if my_snake.parcalar[0].distance(yemek) < 15:
 yemek.kabom()
 skor.puanart()

ekran.exitonclick()
