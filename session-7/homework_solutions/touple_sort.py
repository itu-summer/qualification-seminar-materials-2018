def bubble_sort(data_list):
    """ Bouble sort."""
    for passnum in range(len(data_list) - 1, 0, -1):
        for idx in range(passnum):
            if data_list[idx] > data_list[idx + 1]:
                temp = data_list[idx]
                data_list[idx] = data_list[idx + 1]
                data_list[idx + 1] = temp


def improved_bubble_sort(data_list):
    """ Example of improved bouble sort."""
    for passnum in range(len(data_list) - 1, 0, -1):
        is_sorted = True
        for idx in range(passnum):
            if data_list[idx] > data_list[idx + 1]:
                temp = data_list[idx]
                data_list[idx] = data_list[idx + 1]
                data_list[idx + 1] = temp
                is_sorted = False
        if is_sorted:
            return


def touple_bubble_sort(data_touple, sort_by = 0):
    """ Example of improved bouble sort on touples."""
    for passnum in range(len(data_touple) - 1, 0, -1):
        is_sorted = True
        for idx in range(passnum):
            if data_touple[idx][sort_by] > data_touple[idx + 1][sort_by]:
                temp = data_touple[idx]
                data_touple[idx] = data_touple[idx + 1]
                data_touple[idx + 1] = temp
                is_sorted = False
        if is_sorted:
            return 


def dic_sort(list_of_dicts, key):
    """ Example of improved bouble sort on list of dictionaries."""
    for passnum in range(len(list_of_dicts) - 1, 0, -1):
        is_sorted = True
        for idx in range(passnum):
            if list_of_dicts[idx][key] > list_of_dicts[idx + 1][key]:
                temp = list_of_dicts[idx]
                list_of_dicts[idx] = list_of_dicts[idx + 1]
                list_of_dicts[idx + 1] = temp
                is_sorted = False
        if is_sorted:
            return