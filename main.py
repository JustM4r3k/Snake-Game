import turtle, time, snake, food

import score

x_food = 0
y_food = 0
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("My snake game.")
screen.tracer(0)
turtle.mode("standard")

obj_food = food.Food()

snake = snake.Snake()
snake.spawn()

obj_score = score.Score()

screen.listen()
screen.onkey(key="w", fun=snake.north)
screen.onkey(key="s", fun=snake.south)
screen.onkey(key="d", fun=snake.east)
screen.onkey(key="a", fun=snake.west)


def spawn_food():
    global x_food, y_food
    obj_food.spawn()
    x_food = obj_food.x
    y_food = obj_food.y


obj_score.write_score(snake.score, snake.high_score)
spawn_food()
while True:
    if snake.turtles[0].xcor() > -500 and snake.turtles[0].xcor() < 500 and snake.turtles[0].ycor() > -500 and \
    snake.turtles[0].ycor() < 500:

        if snake.detect_food(x_food, y_food):
            spawn_food()
        snake.inc_h_s()
        obj_score.write_score(snake.score, snake.high_score)
        snake.move()
        snake.detect_yourself()
        screen.update()
        time.sleep(0.1)
    else:
        snake.reset()


screen.exitonclick()
