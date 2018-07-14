import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    """Download a remote file specified by a URL to a
    local directory.

    :param url: str
        URL pointing to a remote file.

    :param to: str
        Local path, absolute or relative, with a filename
        to the file storing the contents of the remote file.
    """

    # TODO: Implement me!
    # None is the same as False in a boolean expression (default value of the
    # variable "to" is None)
    if not to:
        # set the output directory to the current directory
        to = os.getcwd()
        # print(to)
        # an old print statement used while programming to understand the code
    parse_out = urlparse(url)
    # urllib.parse.urlparse() returns a named tuple. You can both access the 
    # entries by sequential index (like a list or tuple) or a key value (a bit
    # like a dictionary but not quite)
    # 
    # print(parse_out[2])
    # print(parse_out.path)
    # print(os.path.split(parse_out.path))
    # print(os.path.join(to, os.path.split(parse_out.path)[1]))
    # 
    # check if the file already exists using os.path.isfile()
    if os.path.isfile(os.path.join(to, os.path.split(parse_out.path)[1])):
        print("File already here.")
        return
    else:
        # download the file if it doesn't exist
        req.urlretrieve(url, 
                filename=os.path.join(to, os.path.split(parse_out.path)[1]))
        # anything inside brackets can be split across lines


if __name__ == 'main':
    url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
    download(url)
