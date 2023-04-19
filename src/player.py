from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """
        Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
        When this happens, return the turtle to the starting position and increase the speed of the cars.
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

