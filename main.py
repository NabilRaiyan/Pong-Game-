from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Pong Game")
screen.bgcolor("white")
screen.setup(width=800, height=650)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(fun=r_paddle.go_up,  key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up,  key="w")
screen.onkey(fun=l_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Detect if the paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        ball.move_speed = 0.1
        score.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        ball.move_speed = 0.1
        score.r_point()


screen.exitonclick()
