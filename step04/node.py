class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(10)
node2 = Node(20)
node1.next=node2
node3 = Node(30)
node2.next=node3

current = node1
while current is not None:
    print(current.data)
    current = current.next