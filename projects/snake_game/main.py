import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


speed = 0.1
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) # turning off the trace left by the moving turtle blocks

# segment_1 = Turtle("square")
# segment_1.color("white")
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()  # to remove trace and show the latest position of turtle blocks
    time.sleep(speed)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        speed -= 0.001
        time.sleep(speed)
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_is_on = False
        #scoreboard.game_over()
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    #for segment in snake.segments:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #instead of using above code, we can use slicing fuctionality
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset_score()
            snake.reset_snake()


screen.exitonclick()