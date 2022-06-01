def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j-=1
    return my_list


if __name__ == '__main__':
    my_list = [1,6,4,34,232,132,2,4,3,5,6]
    print(insertion_sort(my_list))