import string


class TextContainer(object):
    """docstring for TextContainer"""

    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = self.text.split()
        amount_words = len(words)
        return amount_words

    def count_chars(self):
        return len(self.text)

    def count_letters(self):
        count = 0
        for char in self.text:
            if char in string.ascii_letters:
                count += 1
        return count

    def remove_punctuation(self):
        """ Remove punctuation by replacement."""
        for punctuation_char in string.punctuation:
            if punctuation_char in self.text:
                self.text = self.text.replace(punctuation_char, '')
        return self.text


if __name__ == '__main__':

    bones_in_london_txt = '''There was a slump in the shipping market, and men who were otherwise
decent citizens wailed for one hour of glorious war, when Kenyon Line
Deferred had stood at 88 1/2, and even so poor an organization as
Siddons Steam Packets Line had been marketable at 3 3/8.

Two bareheaded men came down the busy street, their hands thrust into
their trousers pockets, their sleek, well-oiled heads bent in dejection.

No word they spoke, keeping step with the stern precision of soldiers.
Together they wheeled through the open doors of the Commercial Trust
Building, together they left-turned into the elevator, and
simultaneously raised their heads to examine its roof, as though in its
panelled ceiling was concealed some Delphic oracle who would answer the
riddle which circumstances had set them.'''

    bones_in_london = TextContainer(bones_in_london_txt)
    print(bones_in_london.count_words())
    print(bones_in_london.count_chars())
    print(bones_in_london.count_letters())
    print(bones_in_london.remove_punctuation())
