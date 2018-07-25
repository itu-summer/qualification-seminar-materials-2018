from turtle import Turtle, done


def draw_bar(t, height, width=20):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape


def draw_sorted(data_list):
    data_list = sorted(data_list)

    bob = Turtle()
    bob.color("green")
    bob.fillcolor("yellow")
    bob.pensize(3)

    for element in data_list:
        draw_bar(bob, element)


def draw_unsorted(data_list):
    tess = Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(2)

    tess.penup()
    tess.backward(250)
    tess.pendown()

    for element in data_list:
        draw_bar(tess, element)


def main():
    data = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
    numerical_data = []
    for element in data:
        numerical_data.append(ord(element))
    print(numerical_data)
    draw_unsorted(numerical_data)
    draw_sorted(numerical_data)
    done()


if __name__ == '__main__':
    main()
