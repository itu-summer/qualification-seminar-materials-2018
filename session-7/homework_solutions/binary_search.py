def binary_search(data, elemelt):
    left = 0
    right = len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if data[middle] == elemelt:
            return middle
        elif data[middle] < elemelt:
            left = middle + 1
        elif data[middle] > elemelt:
            right = middle - 1
    return -1