import turtle
import time
import snake
ekran = turtle.Screen()
ekran.setup(600, 600)
ekran.bgcolor("black")
ekran.title("yılan oyunu")
ekran.tracer(0)
my_snake = snake.Snake()

ekran.listen()
ekran.listen(my_snake.up, "Up")
ekran.listen(my_snake.down, "Down")
ekran.listen(my_snake.left, "Left")
ekran.listen(my_snake.right, "Right")

game_is_on = True
while game_is_on:
 ekran.update()
 time.sleep(0.1)
 my_snake.ileri()

ekran.exitonclick()
