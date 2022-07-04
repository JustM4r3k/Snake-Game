import turtle



class Snake:

    def __init__(self):
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.turtles = []
        self.has_been_pressed = False

    def spawn(self):
        for i in range(4):
            tim = turtle.Turtle(shape="square")
            tim.color("white")
            tim.pu()
            self.turtles.append(tim)
            if len(self.turtles) != 1:
                position = self.turtles[i - 1].xcor()
                self.turtles[i].setx(position - 20)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].xcor(), self.turtles[i - 1].ycor())
        self.turtles[0].forward(20)
        self.has_been_pressed = False

    def south(self):
        if not self.has_been_pressed:
            if self.turtles[0].heading() != 90:
                self.turtles[0].setheading(270)
                self.has_been_pressed = True
            else:
                pass

    def north(self):
        if not self.has_been_pressed:
            if self.turtles[0].heading() != 270:
                self.turtles[0].setheading(90)
                self.has_been_pressed = True
            else:
                pass

    def west(self):
        if not self.has_been_pressed:
            if self.turtles[0].heading() != 0:
                self.turtles[0].setheading(180)
                self.has_been_pressed = True
            else:
                pass

    def east(self):
        if not self.has_been_pressed:
            if self.turtles[0].heading() != 180:
                self.turtles[0].setheading(0)
                self.has_been_pressed = True
            else:
                pass

    def detect_food(self, x, y):
        if self.turtles[0].distance(x, y) < 15:
            tim = turtle.Turtle(shape="square")
            tim.color("white")
            tim.pu()
            self.turtles.append(tim)
            self.score += 1
            return True

    def detect_yourself(self):
        for i in range(3, len(self.turtles)-1):
            if self.turtles[0].distance(self.turtles[i]) < 10:

                for j in range(i, len(self.turtles)-1):
                    if j < len(self.turtles)-1:
                        self.score -= 1
                        self.turtles[j].ht()
                        self.turtles[j].clear()
                        del self.turtles[j]
                return

    def inc_h_s(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def reset(self):
        for i in self.turtles:
            i.goto(1500, 1500)
        self.score = 0
        self.turtles.clear()
        self.spawn()
