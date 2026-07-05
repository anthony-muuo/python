from turtle import Turtle, Screen
from center import CenterLine
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()


screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


game_is_on = True
scoreboard= Scoreboard()
center_line = CenterLine()

while game_is_on:
    time.sleep(ball.accelerate_ball)
    screen.update()
    ball.move()
    # collision with top wall
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y()

    # contact with right paddle
    if (
        ball.distance(right_paddle) < 50 and 
        ball.xcor() > 320 or
        ball.distance(left_paddle) < 50 and
        ball.xcor() < -320
        ):
        ball.bounce_x()
    # detect misses right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect misses left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()