import turtle, random


class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.food = turtle.Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.pu()

    def change_position(self):
        self.x = random.randrange(-480, 480, 20)
        self.y = random.randrange(-480, 480, 20)

    def spawn(self):
        self.change_position()
        self.food.setposition(self.x, self.y)
