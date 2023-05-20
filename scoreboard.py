ALIGNMENT = 'center'
FONT = ('courier',24,'normal')

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0      
       
        self.high_score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
            
        
        self.pensize()
        self.goto(0,265)
        self.color('white')
        self.write(f"Score: {self.score} High Score: {self.high_score}",move=False,align=ALIGNMENT, font=FONT)
        self.hideturtle()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        # self.write(f"Score: {self.score} High score: {self.high_score}",move=False,align='center', font=FONT)
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over",move=False,align=ALIGNMENT,font=FONT)    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",move=False,align='center', font=('arial',24,'normal'))

    
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score    
            with open('data.txt','w') as file:
                file.write(str(self.high_score))
        
        self.score = 0    
        self.update_scoreboard()
  
        