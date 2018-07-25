from cli_text_analysis import find_10_most_common_names
from touple_sort import touple_bubble_sort as touple_sort

def dict_to_touple(data_dict):
    """ Writes a dict as touple."""
    new_touple = []
    for name in data_dict.keys():
        new_touple.append((name,data_dict[name]))
    return new_touple


def sherlock_sort(filename):
    """ Finds the 10 most common names and sort them."""
    with open(filename) as f:
        text = f.read()
    names = find_10_most_common_names(text)
    names_touple = dict_to_touple(names)
    names_sorted = touple_sort(names_touple, 1)
    return names_sorted