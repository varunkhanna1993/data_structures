"""
#Intro 
1. Linked Lists dont have indices 
2. No contiguous place in memory.
3. Nodes are all over the place
4. Imagine nodes and it has a head - first node in the list
5. and tail is the last node in the list
6. each node points to the next one in the list and the tail node does not point to anything thus it points to None

# big O of linked lists 
1. Method append another new node in the last of the list and point tail to the new node
O(1)
2. what if you remove the last node? 
We can remove the last item in the list which would just be O(1) BUT because the tail has to be pointed to the last node, it each to iterate
over all the nodes to find the last node and thus it is
O(n)
3. what if you need to append an item to the starting of the linked list?
Add an item and add new node to the first item and then head points to the first new item.
This would be O(1)
4. What if you need to remove the first item in the linked list
we can do head.next()
and then remove the first item in the list
O(1)
5. what if we have to add it to somewhere in the list
O(n)
6. what if we have to remove something in the middle of the list?
same O(n)
7. Lookup in a linked list?
O(n) but in a list it would be O(1)
8.  
"""

"""
Linked list under the hood
What is a node? 
it is essentially a dictionary, it has a value and has a next value (i.e. the pointer)

"""
