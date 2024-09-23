from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, point, x_cor, y_cor):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        #self.point = 0
        self.goto(x_cor, y_cor)
        self.update_scoreboard(point)

    def update_scoreboard(self, point):
        self.clear()
        self.write(point, align="center", font=("Arial", 80, "normal"))

    def game_over(self, message):
        self.goto(0, 0)
        self.color("orange")
        self.write(f"GAME OVER \n   {message}", align="center", font=("Arial", 50, "normal"))
