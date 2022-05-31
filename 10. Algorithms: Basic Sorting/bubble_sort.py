def bubble_sort(my_list):
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list
my_list = [12,24,1,12,34,12,12,43]
print(bubble_sort(my_list))