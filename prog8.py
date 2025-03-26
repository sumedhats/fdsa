class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # Circular link
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete_node(self, data):
        if not self.head:
            print("List is empty.")
            return
        
        temp = self.head
        prev = None
        
        # If the head node needs to be deleted
        if temp.data == data:
            if temp.next == self.head:  # Only one node in list
                self.head = None
            else:
                while temp.next != self.head:  # Find the last node
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            return
        
        # Search for the node to delete
        curr = self.head
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.data == data:
                prev.next = curr.next
                return
        print("Node not found.")

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to Head)")

# Example usage:
circular_list = CircularLinkedList()
circular_list.insert_at_end(10)
circular_list.insert_at_end(20)
circular_list.insert_at_end(30)
circular_list.display()

circular_list.delete_node(20)
circular_list.display()

