ALIGNMENT = 'center'
FONT = ('courier',24,'normal')

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pensize()
        self.goto(0,265)
        self.color('white')
        self.write(f"Score: {self.score}",move=False,align=ALIGNMENT, font=FONT)
        self.hideturtle()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",move=False,align='center', font=('arial',24,'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game over",move=False,align=ALIGNMENT,font=FONT)    