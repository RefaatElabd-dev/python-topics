class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insertion_sort(self):
        if self.length < 2:
            return
        sorted_list = LinkedList(self.head.value)
        self.head = self.head.next
        while self.head is not None:
            current = self.head
            self.head = self.head.next
            current.next = None
            if current.value < sorted_list.tail.value:
                sorted_list.insert_in_sorted_place(current)
            else: 
                sorted_list.append(current.value)
        self.head = sorted_list.head
   
    def insert_in_sorted_place(self, node):
        if node.value < self.head.value:
            node.next = self.head
            self.head = node
            return
        before = self.head
        current = self.head.next
        while True:
            if node.value >= before.value and node.value <= current.value:
                node.next = current
                before.next = node
                self.length += 1
                break
            before = before.next
            current = current.next
        


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

