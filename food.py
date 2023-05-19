from turtle import Turtle
import random

'''
The Food class represents the food object in the game.
It extends the Turtle class to inherit its attributes and methods.
'''
class Food(Turtle):
    
    def __init__(self):
        super().__init__() #call the parent's init() class
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('deep pink')
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280,280) #Pop up in a random location
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)