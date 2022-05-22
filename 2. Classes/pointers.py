num1 = 11

num2 = num1
print(id(num1), id(num2))
num2 = 22
print(num2, num1)
print(id(num1), id(num2))

## but what happens with dictionary

dict1 = {'value': 11 }

dict2 = dict1

dict2['value'] = 22
print(dict1['value'])


# what happens with lists?

list1  = [1,2,3,4]
list2 = list1

print(list1, list2)

list2.pop()

print(list2, list1)