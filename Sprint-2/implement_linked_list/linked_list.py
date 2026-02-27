class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_head(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        
        return new_node
    
    def pop_tail(self):
        if self.tail is None:
            return None
        
        value = self.tail.value
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        
        return value
    
    def remove(self, node):
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous
        
        node.next = None
        node.previous = None
