class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        pass

    def r_contains(self, value):
        if self.root is None:
            return False
        return self.__r_contains(self.root, value)

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if(current_node.value == value):
            return True
        elif(current_node.value > value):
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)