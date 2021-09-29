from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


LIVES = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while LIVES >= 0:
    snake_alive = True
    LIVES -= 1
    score.snake_dead(LIVES)
    while snake_alive:
        screen.update()
        time.sleep(0.1)
        snake.move()
        snake_alive = snake.detect_collision(screen)
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()
    screen.update()
    if LIVES > 0:
        snake.reset()

screen.update()
#score.game_over()
screen.exitonclick()
