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
    def remove(self):
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
        return temp.value

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
        pass

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
        return temp.value
    
    def pop_first(self):
        if(self.length == 0):
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if(self.length == 0):
            self.tail = None
        return temp.value
    
    def remove(self):
        pass

    def reverse(self):
        pass

    def set(self, index, value):
        pass


    

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

print(myLinkedList.get(3))
print(myLinkedList.get(0))
print(myLinkedList.get(4))
print(myLinkedList.get(5))







