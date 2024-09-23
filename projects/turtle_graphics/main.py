from turtle import Turtle, Screen

leo = Turtle()
leo.color("red")


for _ in range(4):
    leo.forward(100)
    leo.right(90)

screen = Screen()
screen.bgcolor("white")
screen.exitonclick()

