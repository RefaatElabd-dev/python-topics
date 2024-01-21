class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value
        
class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.head is None:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(0, index, 1):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        target_node = self.get(index)
        if target_node is not None:
            target_node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if(index == self.length):
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index)
        new_node.prev = temp.prev
        new_node.next = temp
        temp.prev.next = new_node
        temp.prev = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
        
    def swap_first_last(self):
        if self.head is not None:
            temp_value = self.head.value
            self.head.value = self.tail.value
            self.tail.value = temp_value
    
    def reverse(self):
        temp = self.head
        for _ in range(self.length):
            prev = temp.prev
            temp.prev = temp.next
            temp.next = prev
            temp = temp.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def is_palindrome(self):
        if self.length <= 1:
            return True
        middle = self.length//2
        if(middle * 2 < self.length):
            middle += 1
        right = self.tail
        left = self.head
        for _ in range(middle):
            if(right.value == left.value):
                right = right.prev
                left = left.next
                continue
            return False
        if(right.value == left.value):
            return True
        return False
    
    def swap_pairs(self):
        if self.length > 1:
            temp = self.head
            while(temp is not None and temp.next is not None):
                self.swap(temp, temp.next)
                temp = temp.next.next
        return self.head
    
    def swap(self, node1, node2):
        value = node1.value
        node1.value = node2.value
        node2.value = value

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""