def insertion_sort(data_list):
    for i in range(1,len(data_list)):
        curr_val = data_list[i]
        position = i
        while position > 0 and data_list[position - 1] > curr_val:
            data_list[position] = data_list[position - 1] 
            position = position - 1
        data_list[position] = curr_val