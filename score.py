import turtle


class Score:
    def __init__(self):
        self.text = turtle.Turtle()

        self.text.pu()
        self.text.color("white")
        self.text.goto(0, 470)
        self.text.hideturtle()

    def write_score(self, score, h_score):
        self.text.clear()
        self.text.write(f"Score: {score}   High score: {h_score}", False, "center", ("Arial", 16, "normal"))
        with open("high_score.txt", "w") as file:
            file.write(str(h_score))


