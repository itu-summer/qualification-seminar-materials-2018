import os
import sys
import urllib.request as req
from urllib.parse import urlparse


def download(url):
    local_file = os.path.join('.', os.path.basename(urlparse(url).path))
    print('Downloading file to {}'.format(local_file))

    if not os.path.isfile(local_file):
        # download the file only in case we did not do so earlier
        req.urlretrieve(url, local_file)


def run(arguments):
    if arguments:
        for url in arguments:
            download(url)
    else:
        print('Usage: python download_books.py arg_1 [arg_2 ...]')


if __name__ == '__main__':
    # Call me from the CLI for example with:
    # python args_printer.py arg_1 [arg_2 ...]
    run(sys.argv[1:])
