import os
import sys
from turtle import Turtle, done


def do_line(turtle, command, value):
    value = int(value)
    if command == 'Turn':
        turtle.right(value)
    elif command == 'Walk':
        turtle.forward(value)


def main(path_to_file):

    if os.path.isfile(path_to_file) and path_to_file.endswith('.trtl'):
        my_turtle = Turtle(shape='turtle')

        with open(path_to_file) as file_pointer:
            for line in file_pointer:
                command, value = line.split(' ')
                do_line(my_turtle, command, value)


if __name__ == '__main__':
    main(sys.argv[1])
    done()
