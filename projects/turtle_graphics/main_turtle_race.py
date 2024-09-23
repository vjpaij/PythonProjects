from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,500)
user_bet = screen.textinput(title="Place a bet", prompt="Which colour turtle will win the race?")
colours = ["red", "blue", "yellow", "orange", "purple", "pink"]
y_coordinates = [-100, -60, -20, 20, 60, 100]
is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[turtle_index])
    new_turtle.color(colours[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 215:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You win!! The {turtle.pencolor()} won the race")
            else:
                print(f"You lose!! The {turtle.pencolor()} won the race")

        random_pace = random.randint(1,10)
        turtle.forward(random_pace)


screen.exitonclick()