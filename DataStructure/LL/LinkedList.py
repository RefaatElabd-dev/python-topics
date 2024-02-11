from abc import ABC, abstractmethod

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class DataStructure(ABC):
    @abstractmethod
    def print_list(self):
        pass

    @abstractmethod
    def append(self, value):
        pass
    
    @abstractmethod
    def prepend(self, value):
        pass

    @abstractmethod
    def insert(self, index, value):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def pop_first(self):
        pass
    
    @abstractmethod
    def remove(self, index):
        pass

    @abstractmethod
    def reverse(self):
        pass

    @abstractmethod
    def set(self, index, value):
        pass

    @abstractmethod
    def get(self, index):
        pass




class LinkedList(DataStructure):
    def __init__(self, value) -> None:
        self.length = 1
        self.node = Node(value)
        self.head = self.node
        self.tail = self.node

    def get(self, index):
        if (self.length) <= index or index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)  
        if(self.length == 0):
            self.head = self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def insert(self, index, value):
        if(index == 0):
            return self.prepend(value)
        if(index == self.length):
            return self.append(value)
        prev_node = self.get(index - 1)
        if(prev_node):
            new_node = Node(value)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1
            return True
        return False

    def pop(self):
        if(self.length == 0):
            return None
        pre = self.head
        temp = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if (self.length == 0):
            self.head = self.tail = None
        return temp
    
    def pop_first(self):
        if(self.length == 0):
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if(self.length == 0):
            self.tail = None
        return temp
    
    def remove(self, index):
        if(index == 0):
            self.pop_first()
            return True
        if(index == self.length):
            self.pop()
            return True
        prev_node = self.get(index - 1)
        if(prev_node != None):
            temp = prev_node.next
            prev_node.next = temp.next
            temp.next = None
            self.length -= 1
            return True
        return False

    def reverse(self):
        if(self.tail == None or self.head == self.tail):
            return
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # after
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def set(self, index, value):
        target_node = self.get(index)
        if(target_node):
            target_node.value = value
            return True
        return False
    
    ################## Problems ##################
    ######### Find Middle Node
    def find_middle_node (self):
        slow_ptr = self.head
        fast_ptr = self.head
        while(fast_ptr):
            fast_ptr = fast_ptr.next
            if(fast_ptr):
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
        return slow_ptr
    
    # has_loop
    def has_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while(fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if(fast_ptr == slow_ptr):
                return True
        return False
    
    def bubble_sort(self):
        j = 0
        for i in range(self.length):
            temp = self.head
            while temp.next is not None and j != self.length - i:
                if temp.value > temp.next.value:
                    self.swap(temp, temp.next)
                temp = temp.next
                j += 1
        
    def swap(self, node1, node2):
        node1.value, node2.value = node2.value, node1.value

    def selection_sort(self):
        j = 0
        current = self.head
        for i in range(self.length):
            smallest = current
            inner_current = current.next
            while inner_current is not None:
                if(inner_current.value < smallest.value):
                    smallest = inner_current
                inner_current = inner_current.next
            if (smallest.value != current.value):
                smallest.value, current.value = current.value, smallest.value
            current = current.next
    
    # create insertion sort algorithm for a linked list
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

    def merge(self, other_list):
        compined = LinkedList(0)
        current = compined.head
        while self.head is not None and other_list.head is not None:
            if self.head.value < other_list.head.value:
                compined.append(self.head.value)
                self.head = self.head.next
            else:
                compined.append(other_list.head.value)
                other_list.head = other_list.head.next
                
        while self.head is not None:
            compined.append(self.head.value)
            self.head = self.head.next
            
        while other_list.head is not None:
            compined.append(other_list.head.value)
            other_list.head = other_list.head.next
        
        self.head = compined.head.next
        self.tail = compined.tail
        self.length = compined.length


def find_kth_from_end(ll,  k):
    if(k<=0 or ll.head == None):
        return None
    slow = ll.head
    fast = ll.head
    for _ in range(k-1):
        fast = fast.next
        if(fast == None):
            return None

myLinkedList = LinkedList(1)
myLinkedList.append(5)
myLinkedList.append(17)
myLinkedList.prepend(4)
myLinkedList.print_list()
print(myLinkedList.pop())
print(myLinkedList.pop())
print(myLinkedList.pop())
print(myLinkedList.pop())
print(myLinkedList.pop())

myLinkedList.append(5)
myLinkedList.prepend(1)
myLinkedList.append(17)
myLinkedList.prepend(4)
# print(myLinkedList.pop_first())
# print(myLinkedList.pop_first())
# print(myLinkedList.pop_first())
# print(myLinkedList.pop_first())
# print(myLinkedList.pop_first())

myLinkedList.print_list()
print("after first insertion")
myLinkedList.insert(3, 20)

myLinkedList.print_list()
myLinkedList.insert(2, 10)
print("after second insertion")
myLinkedList.print_list()

myLinkedList.set(3, 18)
print("after override 3rd Node with value 18")
myLinkedList.print_list()

myLinkedList.remove(4)
print("after removing 4th")
myLinkedList.print_list()

print("Reversing ...")
myLinkedList.reverse()
myLinkedList.print_list()







