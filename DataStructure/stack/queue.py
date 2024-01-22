class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class Queue:
    def __init__(self, value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1

    def enqueue(self, value):
        node = Node(value)
        if self.first is None:
           self.first = node
           self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
    
    def dequeue(self):
        if self.first is None:
            return None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        if self.length  == 1:
            self.last = None
        self.length -= 1
        return temp