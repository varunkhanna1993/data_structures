from operator import itemgetter


def items_in_common(list1, list2):
    my_dict ={}
    for items in list1:
        my_dict[items] = True
    for items_j in list2:
        if items_j in my_dict:
            return True
    return False
    # print(my_dict)
list1 = [1,2,3]
list2 = [6,4,3]

print(items_in_common(list1,list2))
