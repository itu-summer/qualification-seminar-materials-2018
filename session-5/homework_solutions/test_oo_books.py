import oo_books as oob
from his_last_bow import TITLE, TOC, CONTENTS


def test_book():
    Library = oob.Library()
    new_contents = oob.read_contents(CONTENTS)
    Library.create_book(TITLE, TOC, new_contents)
    hlb = Library.get_book(0)
    print(new_contents[0])
    print(CONTENTS[0])
    assert hlb.title == TITLE
    assert len(hlb.chapters) == len(TOC)
    for i in range(len(TOC)):
        assert(hlb.open_book(i+1).title) == TOC[i]
        assert(hlb.open_book(i+1).paragraphs[0].lines[0]) == CONTENTS[i][0].split("\n")[0]
        assert(hlb.open_book(i+1).paragraphs[-1].lines[-1]) == CONTENTS[i][-1].split("\n")[-1]
