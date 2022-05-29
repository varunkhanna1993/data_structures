class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """_summary_
        steps involved:
        1. First create a new node
        2. then check if root node is none just insert 
        the node there
        3. temp = self.root (this would be used to traverse through the tree)
        4. while loop (as we dont know how many times we are going to run through)
        if value = node value then return false (edge case)
        if value < node then left otherwise right
        if value is empty then insert there
        Args:
            value (_type_): _description_
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # you dont need the following two lines of code as if its empty,
        #  it wouldn't run the while loop as it will be pointing to None
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

my_tree = BinarySearchTree()
my_tree.insert(45)
my_tree.insert(34)
my_tree.insert(60)
my_tree.insert(20)
my_tree.insert(23)
my_tree.insert(28)
print(my_tree.contains(30))
print(my_tree.min_value_node(my_tree.root).value)
print(my_tree.max_value_node(my_tree.root).value)
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
