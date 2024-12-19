"""
 Day 10: Mastering Data Structures - Stacks and Queues

On Day 10, the focus is on understanding and implementing two fundamental linear data structures: Stacks and Queues. 
These structures form the building blocks for solving many computational problems, making them essential for mastering data structures and algorithms.

Key Learnings for the Day:

Stacks:
Operates on the LIFO (Last In, First Out) principle.
Common operations: Push, Pop, and Peek.
Applications include expression evaluation, undo functionality in editors, and backtracking algorithms.

Queues:
Operates on the FIFO (First In, First Out) principle.
Common operations: Enqueue, Dequeue, and Front.
Applications include task scheduling, data buffering, and breadth-first search.

Double-Ended Queue (Deque):
Allows insertion and deletion at both ends, combining stack and queue functionalities.
Used in sliding window problems, browser navigation history, and BFS optimizations.


Practical Implementation:
Today's focus includes writing Python programs to implement these structures using both basic lists and the collections.deque module.
Each implementation demonstrates key operations with real-world scenarios to solidify understanding.

Outcome:
By the end of the day, you will have a deep understanding of the working, advantages, 
and applications of Stacks and Queues. You'll also appreciate their importance in solving 
algorithmic challenges and be equipped to implement them efficiently in Python.

"""

# Code ------------------------------------------------#

from collections import deque

# Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"Pushed {value} to the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)
        print(f"Enqueued {value} to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue.popleft()

    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

# Demonstration
if __name__ == "__main__":
    # Stack operations
    print("=== Stack Operations ===")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(f"Top element: {stack.peek()}")
    print(f"Popped: {stack.pop()}")
    print(f"Is stack empty? {stack.is_empty()}")

    # Queue operations
    print("\n=== Queue Operations ===")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(f"Front element: {queue.front()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Is queue empty? {queue.is_empty()}")
