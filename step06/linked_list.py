class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next  is not None:
            current = current.next
        current.next = new_node

    def print_list(self):
        current=self.head
        while current is not None:
            print(current.data)
            current = current.next

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def length(self):
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next
        return counter

    def sum(self):
        current = self.head
        total = 0
        while current is not None:
            total += current.data
            current = current.next
        return total

    def max(self):
        if self.head is None:
            return None
        current=self.head
        max_value = current.data
        while current is not None:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

    def prepend(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node



class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

ll = LinkedList()

ll.prepend(30)
ll.prepend(20)
ll.prepend(10)

ll.print_list()