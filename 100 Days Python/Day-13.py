"""

A tree is a hierarchical data structure consisting of nodes, where each node has a value and references to child nodes. 
The topmost node is called the root, and nodes without children are called leaves. 
Trees are widely used in computer science for organizing data in a way that enables efficient searching, insertion, and deletion.


Types of Trees:
Binary Tree: Each node has at most two children.

Binary Search Tree (BST): A binary tree with the property that left children contain values less than the parent, 
and right children contain values greater than the parent.

Full Binary Tree: All nodes have either 0 or 2 children.

Complete Binary Tree: All levels are completely filled except possibly the last, which is filled from left to right.
Balanced Binary Tree: Height of the left and right subtrees differ by at most one.
General Tree: Each node can have an arbitrary number of children.


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# Example Usage
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

print("Inorder Traversal:")
tree.inorder_traversal(tree.root)
