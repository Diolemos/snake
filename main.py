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
#detect collision with food
    if snake.head.distance(food) < 17:
        print("Yammi fruit:P")
        
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#detect collision with wall
    if snake.head.xcor() > 284 or snake.head.xcor() < -284 or snake.head.ycor()>284 or snake.head.ycor()< -284:
        game_is_on = False
        scoreboard.game_over()
    
    for segment in snake.body[1:-1]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()
                

screen.exitonclick()    