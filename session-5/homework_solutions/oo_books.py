class Library():


    def __init__(self):
        """A library contains."""
        self.books = []
        self._num_books = 0


    def put_book(self, book, collection=False):
        """ Insert a single book object into the library."""
        self.book = book
        self.collection = collection
        if collection is True:  # If collections is True Then book is a list
            for new_book in self.book:
                self.books.append(new_book)
                self._num_books += 1
        else:
            self.books.append(self.book)
            self._num_books += 1


    def __repr__(self):
        return 'The size of the library is %r' % (self._num_books)


    def __str__(self):
        return 'The size of the library is {size}.'.format(
            size=self._num_books)


    def read(self, book_idx=None):
        """ See what the library contains."""
        print("The books in this library are")
        for idx, cur_book in enumerate(self.books):
            print(cur_book.title, "\t with the book_idx of: ", idx)


    def create_book(self, title, toc, contents, author="Edgar Allan Poe"):
        """ Create and insert a book object into the library."""
        book_chapters = []
        for i in range(len(toc)):
            chap = Chapter(i + 1, toc[i], contents[i])
            book_chapters.append(chap)
        book = Book(title, author, book_chapters)
        self.books.append(book)
        self._num_books += 1


    def get_book(self, book_idx=0):
        """ Get a book by index."""
        return self.books[book_idx]


class Book():
    """A simple book model consisting of chapters, which in
    turn consist of paragraphs."""


    def __init__(self, title, author, chapters=[]):
        """Initialize title, the author, and the chapters."""
        self.title = title
        self.author = author
        self.chapters = chapters


    def __repr__(self):
        return 'Book(%r, %r, %r)' % (self.title, self.author,
                                     self.chapters)


    def __str__(self):
        return '{name} by {by} has {nr_chap} chapters.'.format(
            name=self.title, by=self.author, nr_chap=len(self.chapters))


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


    def __repr__(self):
        return 'Chapter(%r, %r, %r)' % (self.number, self.title,
                                        self.paragraphs)


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
        self._reading_position = 0


    def read(self):
        """Simulate reading a i single line in a paragraph 
            by printing its contents.""" 
        print(self.lines[self._reading_position])


    def read_all(self):
        """Simulate reading a paragraph by printing its contents.""" 
        for line in self.lines:
            print(line)


    def get_reading_position(self):
        return self._reading_position
    

    def _update_reading_position(self, new_position):
        if new_position <= len(self.lines) - 1:
            self._reading_position = new_position
          

    def scroll_down(self):
        if self._reading_position < len(self.lines) - 1:
            self._reading_position += 1
        else:
            self._reading_position = 0
            
            
    def scroll_up(self):
        if self._reading_position >= 1:
            self._reading_position -= 1
        else:
            self._reading_position = len(self.lines) - 1


def read_contents(contents):
    new_contents = []
    for i in range(len(contents)):
        new_chapter = []
        for j in range(len(contents[i])):
            new_pragraph = contents[i][j].split("\n")
            new_chapter.append(new_pragraph)
        new_contents.append(new_chapter)
    return new_contents


if __name__ == '__main__':
    from his_last_bow import TITLE, TOC, CONTENTS


    """ Example of use."""
    Library = Library()
    CONTENTS = read_contents(CONTENTS)
    Library.create_book(TITLE, TOC, CONTENTS)
    hlb = Library.get_book(0)
    chapter_1 = Chapter(1, 'Bones and Big Business', 
                        ["bljshdfg","bklajswkabsd"])
    chapter_2 = Chapter(2, 'Hidden Treassure', 
                        ["lkd lsadmf \n lsdnf lisdf","bklajswkabsd"])
    book = Book('Bones in London', 'Edgar Wallace',
                [chapter_1, chapter_2])
    Library.put_book(book)
    Library.get_book(0).read() # Reads the entire first chapter from first book
    
    # Read first paragrah in first chapter
    Library.get_book(0).open_book(chapter=1).read(0)
