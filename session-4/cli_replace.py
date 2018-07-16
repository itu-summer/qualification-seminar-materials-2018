"""
Adapted from: https://wiki.python.org/moin/Powerful%20Python%20One-Liners
"""
import sys


if __name__ == '__main__':
    # Call me from the CLI for example with:
    # printf "My cat looks weirdly.\nThe neighbours cat too...\n" | python cli_replace.py cat dog
    pattern = sys.argv[1]
    substitution = sys.argv[2]

    for line in sys.stdin:
        sys.stdout.write(line.replace(pattern, substitution))
