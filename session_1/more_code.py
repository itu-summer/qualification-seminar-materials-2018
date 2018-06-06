import sys


def say(message):
    return f'You said {message}'


if __name__ == '__main__':
    say(sys.argv[1])
