from text_container import TextContainer


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


def test_count_words():
    assert bones_in_london.count_words() == 130


def test_count_chars():
    assert bones_in_london.count_chars() == 790


def test_count_letters():
    assert bones_in_london.count_letters() == 634


def test_remove_punctuation():
    text_wo_punctuation = '''There was a slump in the shipping market and men who were otherwise
decent citizens wailed for one hour of glorious war when Kenyon Line
Deferred had stood at 88 12 and even so poor an organization as
Siddons Steam Packets Line had been marketable at 3 38

Two bareheaded men came down the busy street their hands thrust into
their trousers pockets their sleek welloiled heads bent in dejection

No word they spoke keeping step with the stern precision of soldiers
Together they wheeled through the open doors of the Commercial Trust
Building together they leftturned into the elevator and
simultaneously raised their heads to examine its roof as though in its
panelled ceiling was concealed some Delphic oracle who would answer the
riddle which circumstances had set them'''

    assert bones_in_london.remove_punctuation() == text_wo_punctuation