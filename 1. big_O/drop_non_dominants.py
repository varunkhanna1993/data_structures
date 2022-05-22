def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
print_items(10)

# this would be n^2 +n but we would just write it as O(n^2)