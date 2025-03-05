class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def delete_node(self, data):
        current = self.head
        
        # If the node to be deleted is the head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        
        # If the node with the given data is not found
        if current is None:
            return
        
        prev.next = current.next
        current = None
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()  # For newline after traversal
