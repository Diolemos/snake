from snake import Snake
from food import Food
import time
from turtle import Screen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
game_is_on = True 

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')




while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.head.distance(food) < 15:
        print("Yammi fruit:P")
        food.refresh()




screen.exitonclick()    