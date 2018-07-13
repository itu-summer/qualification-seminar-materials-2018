# stealing the code from count_words_chars.py

import moby_dick as md
copy_pasta = '''
Lady Presenter: Well, it's nothing very special. Try to be nice to people, avoid eating fat, read a good book every now and then, get some walking in, and try and live together in peace and harmony with people of all creeds and nations. And, finally, here are some completely gratuitous pictures of penises to annoy the censors and to hopefully spark some sort of controversy, which it seems is the only way these days to get the jaded, video-sated public off their fucking arses and back in the sodding cinema. Family entertainment? Bollocks. What they want is filth: people doing things to each other with chainsaws during tupperware parties, babysitters being stabbed with knitting needles by gay presidential candidates, vigilante groups strangling chickens, armed bands of theatre critics exterminating mutant goats. Where's the fun in pictures? Oh, well, there we are. Here's the theme music. Goodnight.
'''


def make_headline(input_text, first, last):  # input is already a function
    """
    Takes a string in input_text and finds the words from first to last, both inclusive
    First and last are integers
    """
    # string.strip() removes whitespace from beginning and end of string,
    # string.split() splits a string into a list of strings using whitespace
    # to find where to split
    words = input_text.strip().split()
    # index starts at zero in Python and does not include the end of the range
    # so we slice from first-1 to last - in essence shifting it by one
    first_to_last = words[first - 1:last]
    # make an empty string without any characters, not even whitespace
    headline = ''
    for word in first_to_last:
        # concatenate the entries in a list to a single string,
        # reformatting each one as we go and adding a space
        headline += word.title() + " "
    print(headline)


if __name__ == '__main__':
    text = md.CHAPTER_1[0]
    make_headline(text, 1, 6)
