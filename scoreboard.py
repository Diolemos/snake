from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pensize()
        self.goto(0,269)
        self.color('white')
        self.write(f"Score: {self.score}",move=False,align='center', font=('arial',24,'normal'))
        self.hideturtle()
        