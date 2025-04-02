# Activity 6: 
Write a program to create a class Node to represent a node in a singly linked list. Each node  should have two attributes: data and next. Then, create a class Queue to represent the queue  itself. Implement the following operations: 
1. enqueue(data): Add a new node with the given data to the end of the queue. 
2. Front(): Return the data of the front node without removing it. If the queue is empty, return  None. 
3. is_empty(): Return True if the queue is empty, otherwise return False. 
4. dequeue(): Remove and return the front node from the queue. If the queue is empty, return  None. 
Additionally, implement a function serve_customers() to simulate a customer service queue: 
- Enqueue 5 customers with IDs: 101, 102, 103, 104, and 105. 
- Serve customers by dequeuing one at a time and printing the ID of the customer being served. - After serving all customers, check if the queue is empty and display an appropriate message.
 class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """Represents a queue using a linked list."""
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, data):
        """Add a new node with the given data to the end of the queue."""
        new_node = Node(data)
        if self.is_empty():
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def front(self):
        """Return the data of the front node without removing it."""
        if self.is_empty():
            return None
        return self.front_node.data

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front_node is None

    def dequeue(self):
        """Remove and return the front node from the queue."""
        if self.is_empty():
            return None
        dequeued_data = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node is None:  # If the queue becomes empty
            self.rear_node = None
        return dequeued_data

def serve_customers():
    """Simulates a customer service queue."""
    customer_queue = Queue()

    # Enqueue 5 customers
    customer_ids = [101, 102, 103, 104, 105]
    for customer in customer_ids:
        customer_queue.enqueue(customer)
        print(f"Customer {customer} added to queue.")

    print("\nServing customers...\n")

    # Serve customers by dequeuing one at a time
    while not customer_queue.is_empty():
        served_customer = customer_queue.dequeue()
        print(f"Serving customer {served_customer}.")

    # Check if the queue is empty
    if customer_queue.is_empty():
        print("\nAll customers have been served. The queue is empty.")

# Run the simulation
serve_customers()

