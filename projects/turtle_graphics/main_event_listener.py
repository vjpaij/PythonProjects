from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def move_anticlockwise():
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    tim.left(10)
def move_clockwise():
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=move_anticlockwise,key="a")
screen.onkey(fun=move_clockwise,key="d")
screen.onkey(fun=clear_drawing,key="space")

screen.exitonclick()