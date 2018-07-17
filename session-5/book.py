class Book():
    """A simple book model consisting of chapters, which in 
    turn consist of paragraphs."""

    def __init__(self, title, author, chapters=[]):
        """Initialize title, the author, and the chapters."""
        self.title = title
        self.author = author
        self.chapters = chapters

    def read(self, chapter=1):
        """Simulate reading a chapter, by calling the reading 
        method of a chapter."""
        self.chapters[chapter - 1].read()

    def open_book(self, chapter=1):
        """Simulate opening a book, which returns a chapter 
        object."""
        return self.chapters[chapter - 1]


class Chapter():

    def __init__(self, number, title, paragraphs):
        """A chapter consists of multiple paragraphs."""
        self.number = number
        self.title = title
        self.paragraphs = []
        for paragraph_lines in paragraphs:
            new_pragraph = Paragraph(paragraph_lines)
            self.paragraphs.append(new_pragraph)

    def read(self, paragraph_idx=None):
        """A paragraph can be read."""
        if paragraph_idx != None:
            self.paragraphs[paragraph_idx].read_all()
        else:
            for paragraph in self.paragraphs:
                paragraph.read_all()


class Paragraph():
    """A paragraph consists of a list of lines."""

    def __init__(self, lines):
        """Initialize name and age attributes."""
        self.lines = lines
        self.reading_position = 0

    def read(self):
        """Simulate reading a single line in a paragraph 
            by printing its contents."""
        print(self.lines[self.reading_position])

    def read_all(self):
        """Simulate reading a paragraph by printing its contents."""
        for line in self.lines:
            print(line)

    def get_reading_position(self):
        return self.reading_position

    def update_reading_position(self, new_position):
        if new_position <= len(self.lines) - 1:
            self.reading_position = new_position

    def scroll_down(self):
        if self.reading_position < len(self.lines) - 1:
            self.reading_position += 1
        else:
            self.reading_position = 0

    def scroll_up(self):
        if self.reading_position >= 1:
            self.reading_position -= 1
        else:
            self.reading_position = len(self.lines) - 1
