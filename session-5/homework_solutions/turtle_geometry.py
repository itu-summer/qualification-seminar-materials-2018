from turtle import Turtle, done


class GeometryTurtle(Turtle):

    def make_square(self, width):
        for i in range(4):
            self.right(90)
            self.forward(width)

    def make_rectangle(self, width, height):
        for i in range(2):
            self.forward(width)
            self.right(90)
            self.forward(height)
            self.right(90)

    def make_triangle(self, length):
        for i in range(3):
            self.forward(length)
            self.right(120)

    def make_star(self, length):
        for i in range(5):
            self.forward(length)
            self.right(144)


def main():
    my_turtle = GeometryTurtle()
    my_turtle.make_square(50)

    my_turtle.penup()
    my_turtle.forward(70)
    my_turtle.pendown()

    for i in range(6):
        my_turtle.right(60)
        my_turtle.make_square(30)

    my_turtle.penup()
    my_turtle.forward(70)
    # my_turtle.right(100)
    my_turtle.pendown()

    my_turtle.make_rectangle(50, 20)

    my_turtle.penup()
    my_turtle.forward(70)
    # my_turtle.right(100)
    my_turtle.pendown()

    my_turtle.make_triangle(50)

    my_turtle.penup()
    my_turtle.forward(70)
    # my_turtle.right(100)
    my_turtle.pendown()

    my_turtle.make_star(49)

    # The call to the function `done` from the `turtle` module means that you
    # Have to close the window manually
    done()


if __name__ == '__main__':
    main()
