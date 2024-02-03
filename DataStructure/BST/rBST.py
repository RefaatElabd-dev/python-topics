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

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)
        
    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def delete_node(self, value):
        if self.root is None:
            return None
        self.__delete_node(self.root, value)
    
    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                current_node.value = self.min_value(current_node.right)
                self.__delete_node(current_node.right, current_node.value)
                return current_node

# test (r_insert)
def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Insert into an empty tree -----\n")
bst = BinarySearchTree()
print("Inserting value:", 5)
bst.r_insert(5)
check(5, bst.root.value, "Root value after inserting 5:")
check(None, bst.root.left, "Left child of root:")
check(None, bst.root.right, "Right child of root:")

print("\n----- Test: Insert values in ascending order -----\n")
bst = BinarySearchTree()
values = [1, 2, 3, 4, 5]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(1, bst.root.value, "Root value:")
check(2, bst.root.right.value, "Right child of root:")
check(3, bst.root.right.right.value, "Right child of right child of root:")
check(4, bst.root.right.right.right.value, "Right child's right child's right child of root:")
check(5, bst.root.right.right.right.right.value, "Fourth right child of root:")

print("\n----- Test: Insert values in descending order -----\n")
bst = BinarySearchTree()
values = [5, 4, 3, 2, 1]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(5, bst.root.value, "Root value:")
check(4, bst.root.left.value, "Left child of root:")
check(3, bst.root.left.left.value, "Left child of left child of root:")
check(2, bst.root.left.left.left.value, "Left child's left child's left child of root:")
check(1, bst.root.left.left.left.left.value, "Fourth left child of root:")

print("\n----- Test: Insert values in mixed order -----\n")
bst = BinarySearchTree()
values = [3, 1, 4, 5, 2]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(3, bst.root.value, "Root value:")
check(1, bst.root.left.value, "Left child of root:")
check(2, bst.root.left.right.value, "Right child of left child of root:")
check(4, bst.root.right.value, "Right child of root:")
check(5, bst.root.right.right.value, "Right child of right child of root:")

print("\n----- Test: Insert duplicate values -----\n")
bst = BinarySearchTree()
values = [3, 3, 3]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(3, bst.root.value, "Root value:")
check(None, bst.root.left, "Left child of root:")
check(None, bst.root.right, "Right child of root:")






# test delete

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


# test_delete_node_no_children
print("\n----- Test: Delete node with no children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(None, bst.root.left, "Left child of root after deleting 3:")


# test_delete_node_only_left_child
print("\n----- Test: Delete node with only left child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(1, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_node_only_right_child
print("\n----- Test: Delete node with only right child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(8)
check(9, bst.root.right.value, "Right child of root after deleting 8:")


# test_delete_node_two_children
print("\n----- Test: Delete node with two children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1, 4, 7, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(4, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_root
print("\n----- Test: Delete root -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(5)
check(8, bst.root.value, "Root value after deleting 5:")


# test_delete_non_existent_node
print("\n----- Test: Attempt to delete a non-existent node -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
original_root_value = bst.root.value
bst.delete_node(10)
check(original_root_value, bst.root.value, "Root value after attempting to delete 10:")
