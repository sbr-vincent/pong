from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
scoreboard = Scoreboard()

screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()
#   Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

#   Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#   Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_l_score()

    #   Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_r_score()


screen.exitonclick()
