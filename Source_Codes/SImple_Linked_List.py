# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # store data
        self.next = None  # point to the next node

# Create two nodes
node1 = Node("First")
node2 = Node("Second")
node3=Node("Three")

# Link the nodes
node1.next = node2
node2.next=node3

# Traverse and print the list
current = node1
while current:
    print(current.data)
    current = current.next
