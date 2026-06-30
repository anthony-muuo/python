from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 500)
screen.listen()
screen.bgcolor("black")
screen.title("Snake Game")
# screen to be off when the positions are been created
screen.tracer(0)

snake = Snake()

# controlling the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    # show what happened when the screen was off
    screen.update()
    time.sleep(0.15)

    snake.move()


screen.exitonclick()