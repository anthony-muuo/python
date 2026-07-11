from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.listen()
screen.bgcolor("black")
screen.title("Snake Game")
# screen to be off when the positions are been created
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# controlling the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    # show what happened when the screen was off
    screen.update()
    time.sleep(0.1)
    snake.move()
    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # collison with wall
    if (
        snake.head.xcor() > 290 or 
        snake.head.xcor() < -290 or
        snake.head.ycor() > 290 or
        snake.head.ycor() < -290
    ):
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()