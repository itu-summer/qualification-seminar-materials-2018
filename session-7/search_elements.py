def find_element_in_a_list(data_list, element):
    for idx, el in enumerate(data_list):
        if el == element:
            return idx


def find_element_double_loop(data_list, element):
    for idx, el in enumerate(data_list):
        if el == element:
            first_result_idx = idx
            break
    for idx, el in enumerate(data_list):
        if el == element and idx == first_result_idx:
            return idx, el


def find_element_nested_loop(data_list, element):
    for idx, el in enumerate(data_list):
        for idx2, el2 in enumerate(data_list):
            if el == el2 == element and idx == idx2:
                print(idx, idx2)
                return idx


def find_element_recursive_half(data_list, element):
    half_idx = len(data_list) // 2
    print(len(data_list), half_idx, data_list[half_idx])
    if element == data_list[half_idx]:
        return half_idx, data_list[half_idx]
    elif element < data_list[half_idx]:
        lower_half_list = list(data_list[:half_idx])
        return find_element_in_a_list(lower_half_list, element)
    elif element > data_list[half_idx]:
        upper_half_list = list(data_list[half_idx:])
        return find_element_in_a_list(upper_half_list, element)


if __name__ == '__main__':
    print(find_element_recursive_half(range(10000), 9999))
