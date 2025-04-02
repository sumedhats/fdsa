class Node: 
 def __init__(self, data): 
 self.data = data 
 self.next = None 
class Queue: 
 def __init__(self): 
 self.front_node = None 
 self.rear_node = None 
 def enqueue(self, data): 
 new_node = Node(data) 
 if self.is_empty(): 
 self.front_node = self.rear_node = new_node 
 else: 
 self.rear_node.next = new_node 
 self.rear_node = new_node 
 def front(self): 
 if self.is_empty(): 
 return None 
 return self.front_node.data
38 
CS1082: Fundamentals of Data Structures and Algorithms (2024–2025) 
 def is_empty(self): 
 return self.front_node is None 
# Example usage: 
q = Queue() 
# Enqueue elements 
q.enqueue(10) 
q.enqueue(20) 
q.enqueue(30) 
# Front element 
print("Front element:", q.front()) 
 # Check if queue is empty 
print("Is the queue empty?", q.is_empty()) # Check if queue is empty again 
print("Is the queue empty?", q.is_empty()) 

