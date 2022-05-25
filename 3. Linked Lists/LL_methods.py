#now imagine if 4 methods of a class are creating new nodes, it is best to have a class of create a new node and get in functions from the same
class Node: 
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
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
        
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length = self.length -1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        
    #creates new node to the beginning  
    def prepend(self, value):
        pass        
    #creates new node and inserts that at a given index 
    def insert(self,index, value):
        pass
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("This linked list has a length of", self.length)


#### tests
my_linked_list = LinkedList(4)
my_linked_list.append(23)
my_linked_list.print_list()
print(my_linked_list.pop())
my_linked_list.pop()
my_linked_list.pop()
# print(my_linked_list.length)
my_linked_list.print_list()


