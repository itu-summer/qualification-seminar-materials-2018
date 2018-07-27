import os
import sys
from adts import Stack


def get_file_contents_as_list(path_to_file):
    with open(path_to_file) as fp:
        lines = fp.readlines()
    return lines


def check_params(lines):
    parenthesis_stack = Stack()
    for idx, line in enumerate(lines):
        for cidx, character in enumerate(line):
            if character == '(':
                parenthesis_stack.push(character)
            elif character == ')' and not parenthesis_stack.is_empty():
                parenthesis_stack.pop()
            elif character == ')' and parenthesis_stack.is_empty():
                print(f'You have are closing a parenthesis without opening one on line {idx} on position {cidx}')
                return False
    if parenthesis_stack.is_empty():
        return True
    else:
        return False


def main(path_to_file):
    content_lines = get_file_contents_as_list(path_to_file)
    error = check_params(content_lines)
    if error:
        print('I think all parenthesis are balanced.')
    else:
        print('Looks like you forgot to close some parenthesis...')


if __name__ == '__main__':
    path_to_file = sys.argv[1]
    if os.path.isfile(path_to_file):
        main(path_to_file)
    else:
        print(f'Error, the file {path_to_file} does not exist.')
