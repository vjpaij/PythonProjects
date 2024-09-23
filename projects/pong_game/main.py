from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(380,0)
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

r_paddle = Paddle(380,0)
l_paddle = Paddle(-380,0)
ball = Ball()
l_point = 0
r_point = 0
l_score = Scoreboard(l_point, -100, 200)
r_score = Scoreboard(r_point, 100, 200)


screen.listen()
screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #make ball to bounce
        ball.bounce_y()

    # Detect collision with the paddle
    if ((ball.distance(r_paddle) < 50 and ball.xcor() > 360) or
            (ball.distance(l_paddle) < 50 and ball.xcor() < -360)) :
        ball.bounce_x()

    # Ball misses Right Paddle
    if ball.xcor() > 390:
        ball.reset_position()
        l_point += 1
        l_score.update_scoreboard(l_point)

    # Ball misses Right Paddle
    if ball.xcor() < -390:
        ball.reset_position()
        r_point += 1
        r_score.update_scoreboard(r_point)

    if l_point == 3:
        game_is_on = False
        l_score.update_scoreboard(l_point)
        r_score.update_scoreboard(r_point)
        l_score.game_over("Left Wins")
    elif r_point == 3:
        game_is_on = False
        l_score.update_scoreboard(l_point)
        r_score.update_scoreboard(r_point)
        r_score.game_over("Right Wins")





screen.exitonclick()