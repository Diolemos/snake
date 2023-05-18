from turtle import Turtle
class Snake:
    def __init__(self):
        self.body = []
        self.create_body()
        self.head = self.body[0]       
    def create_body(self):
        x_axis = 0
        for _ in range(3):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(x=x_axis,y=0)
            self.body.append(new_segment)
            x_axis += 20
        
    def move(self):
        for index in range(len(self.body)-1,0,-1):
            new_x = self.body[index -1].xcor()
            new_y = self.body[index -1].ycor() 
            self.body[index].goto(new_x,new_y) 
        self.body[0].fd(20)     
    
    
    def up(self):
        self.head.setheading(90)
        
    def down(self): 
        self.head.setheading(270)
    
    def  left(self):  
        self.head.setheading(180)    
        
    def right(self): 
        self.head.setheading(00)        
            