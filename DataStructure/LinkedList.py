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







