from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scr = Screen()
scr.bgcolor("black")
scr.title("Pong")
scr.setup(width=1000, height=600)
scr.tracer(0)

r_paddle = Paddle((480, 0))
l_paddle = Paddle((-480, 0))
ball = Ball()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(r_paddle.go_up, "Up")
scr.onkey(r_paddle.go_down, "Down")
scr.onkey(l_paddle.go_up, "w")
scr.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    scr.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball. xcor() > 450 or ball.distance(l_paddle) < 50 and ball. xcor() < -450:
        ball.bounce_x()

    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.right_score()

    if ball.xcor() < -480:
        ball.reset_position()
        scoreboard.left_score()

scr.exitonclick()
