import os
import download_books


def test_download():
    frankenstein_url = 'https://www.gutenberg.org/files/84/84-0.txt'
    download_books.download(frankenstein_url)
    assert os.path.isfile('84-0.txt')
    os.remove('84-0.txt')


def test_run():
    frankenstein_url = 'https://www.gutenberg.org/files/84/84-0.txt'
    alice_in_wonderland_url = 'https://www.gutenberg.org/files/11/11-0.txt'
    jekyll_hyde_url = 'https://www.gutenberg.org/files/43/43-0.txt'
    urls = [frankenstein_url, alice_in_wonderland_url, jekyll_hyde_url]

    # Execute the actual function that we want to test
    download_books.run(urls)
    for url in urls:
        file_name = os.path.basename(url)
        assert os.path.isfile(file_name)
        os.remove(file_name)
