class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
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
        temp = self.root
        while temp is not None:
            if value == temp.value: return True
            elif value < temp.value: temp = temp.left
            else: temp = temp.right
        return False
        
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    def is_valid_bst(self):
        tree_in_order_values = self.dfs_in_order()
        return tree_in_order_values == sorted(tree_in_order_values)

    def kth_smallest(self, k):
        if(self.root is None or k < 1):
            return None
        smallest_values = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if(len(smallest_values) < k):
                smallest_values.append(current_node.value)
            else: 
                return
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return None if len(smallest_values) < k else smallest_values[len(smallest_values) - 1]

    def kth_smallest2(self, k):
        stack = []
        node = self.root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.value
            
            node = node.right
            
        return None


##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################


# def check(expect, actual, message):
#     print(message)
#     print("EXPECTED:", expect)
#     print("RETURNED:", actual)
#     print("PASS" if expect == actual else "FAIL", "\n")

# print("\n----- Test: Contains on Empty Tree -----\n")
# bst = BinarySearchTree()
# result = bst.contains(5)
# check(False, result, "Check if 5 exists in an empty tree:")

# print("\n----- Test: Contains Existing Value -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# bst.insert(15)
# result = bst.contains(10)
# check(True, result, "Check if 10 exists:")
# result = bst.contains(5)
# check(True, result, "Check if 5 exists:")
# result = bst.contains(15)
# check(True, result, "Check if 15 exists:")

# print("\n----- Test: Contains Not Existing Value -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# result = bst.contains(15)
# check(False, result, "Check if 15 exists:")

# print("\n----- Test: Contains with Duplicate Inserts -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(10)
# result = bst.contains(10)
# check(True, result, "Check if 10 exists with duplicate inserts:")

# print("\n----- Test: Contains with Left and Right -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# bst.insert(15)
# bst.insert(1)
# bst.insert(8)
# bst.insert(12)
# bst.insert(20)
# result = bst.contains(1)
# check(True, result, "Check if 1 exists:")
# result = bst.contains(8)
# check(True, result, "Check if 8 exists:")
# result = bst.contains(12)
# check(True, result, "Check if 12 exists:")
# result = bst.contains(20)
# check(True, result, "Check if 20 exists:")

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())
print(sorted(my_tree.dfs_post_order()))
print(my_tree.is_valid_bst())


