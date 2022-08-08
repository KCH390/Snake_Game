from turtle import Turtle


class Snake:
    def __init__(self):
        self.LOCATIONS = [(0, 0), (-30, 0), (-50, 0)]
        self.parts = []
        self.snake_bldr()
        self.head = self.parts[0]

    def segment_generator(self, location):
        if self.parts == []:
            piece = Turtle(shape="triangle")
            piece.color("blue")
            piece.shapesize(stretch_len=1.7,stretch_wid=1.7) # Maybe implement gif head?
        else:
            piece = Turtle(shape="square")
            piece.shapesize(stretch_len=1, stretch_wid=1)
            piece.color("blue")
        piece.penup()
        piece.goto(location)
        return piece

    def snake_bldr(self):
        for position in self.LOCATIONS:
            piece = self.segment_generator(position)
            self.parts.append(piece)

    def seg_adder(self):
        piece = self.segment_generator(self.parts[-1].pos())
        self.parts.append(piece)
        piece = self.segment_generator(self.parts[-1].pos())
        self.parts.append(piece)
        piece = self.segment_generator(self.parts[-1].pos())
        self.parts.append(piece)
        piece = self.segment_generator(self.parts[-1].pos())
        self.parts.append(piece)
        piece = self.segment_generator(self.parts[-1].pos())
        self.parts.append(piece)

    def move(self,speed):
        self.head.forward(speed)
        for piece in range(len(self.parts) - 1, 0, -1):
            xloc = self.parts[piece - 1].xcor()
            yloc = self.parts[piece - 1].ycor()
            self.parts[piece].goto(xloc, yloc)

    def left(self):
        if self.head.heading() == 0: pass
        else:self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180: pass
        else: self.head.setheading(0)

    def up(self):
        if self.head.heading() == 270: pass
        else: self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90: pass
        else: self.head.setheading(270)