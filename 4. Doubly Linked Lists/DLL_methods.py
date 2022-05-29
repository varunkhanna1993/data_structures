#now imagine if 4 methods of a class are creating new nodes, it is best to have a class of create a new node and get in functions from the same
class Node: 
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    #creates the new node
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length  = 1

    #create new node to the end
    def append(self, value):
        #1.create new node 
        #2. point the pointer of the last node to the new node
        #3. point the tail to the new node
        #4. edge case where the head and tail are pointing to None, i.e. empty LL, then point both head and tail to the new list
        new_node = Node(value)
        # so we should first cover the edge case
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #now if there are any other nodes in the list
        else:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
        self.length+=1
        #we are gonna write another method which would rely on this append method and that requires this method to return true or false
        return True

    def pop(self):
        """this method returns the last node that has been popped.
        It takes into account 2 edge cases
        1. When the list is empty
        2. When the list has only one node in which case it sets the head and tail to be none. 
        Returns:
            node object: temp node is returned which is the last node currently being popped by this method. 
        """
        # first point tail to the last -1 node
        # the only way to do that is first start at the head and then reach the end-1 of the list 
        if self.length == 0:
            return None
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length = self.length -1
        return temp

    #creates new node to the beginning  
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head  = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head 
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length = self.length -1
        return temp
    
    def get(self, index):
        if index >= self.length or index < 0:
            return None
        temp = self.head
        # if its in the first half, we run the for loop as usual for singly linked list
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        # if its in the second half, then we start from the tail so that we can optimise it. 
        else:
            temp = self.tail 
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):

        ### one method to write the set value method
        # if index <0 or index >=self.length:
        #     return None
        # temp = self.head 
        # for _ in range(index):
        #     temp = temp.next
        # temp.value = value
        # return temp
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    #creates new node and inserts that at a given index 
    def insert(self,index, value):
        if index <0 or index > self.length:
            return False 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before  = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length +=1
        return True
    

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            temp = self.pop_first()
            return temp
        if index == self.length -1:
            temp = self.pop()
            return temp
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None

        self.length = self.length -1
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("This linked list has a length of", self.length)

if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(7)
    print("=============")
    my_doubly_linked_list.append(5)
    my_doubly_linked_list.append(23)
    # my_doubly_linked_list.pop()
    # my_doubly_linked_list.pop()
    # my_doubly_linked_list.pop()
    my_doubly_linked_list.prepend(2312)
    # my_doubly_linked_list.pop_first()
    # print(my_doubly_linked_list.pop_first())
    # my_doubly_linked_list.pop_first()
    # print(my_doubly_linked_list.get(2).value)
    my_doubly_linked_list.insert(2,550000)
    print(my_doubly_linked_list.remove(2).value)
    my_doubly_linked_list.print_list()