"""

This code provides:

Singly Linked List: Operations for adding and displaying elements.
Doubly Linked List: Bidirectional traversal.
Circular Linked List: Circular connections with a display loop

"""

class Node:
    """Node class for general Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # For Doubly Linked List

# 1. Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 2. Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next

        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# 3. Circular Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("HEAD")

# Testing
print("Singly Linked List:")
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()

print("\nDoubly Linked List:")
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward()
dll.display_backward()

print("\nCircular Linked List:")
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.display()
