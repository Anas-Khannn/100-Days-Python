"""
A binary tree is a hierarchical data structure where each node has at most two children, referred to as the left child and the right child. 
Binary trees are foundational structures in computer science, widely used for searching, sorting, and hierarchical data representation.

Key Characteristics:

Root Node: The topmost node of the binary tree.
Child Nodes: Each node has zero, one, or two child nodes.
Parent Node: The node that connects to its child nodes.
Leaf Node: Nodes with no children.
Height: The number of edges on the longest path from the root to a leaf.
Depth: The number of edges from the root to the given node.

Types of Binary Trees:

Full Binary Tree: Every node has either 0 or 2 children.
Perfect Binary Tree: All internal nodes have two children, and all leaf nodes are at the same level.
Complete Binary Tree: All levels except possibly the last are completely filled, and all nodes are as far left as possible.
Binary Search Tree (BST): A binary tree where the left child contains only nodes with keys lesser than the parent node, 
and the right child contains only nodes with keys greater than the parent.



"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def in_order_traversal(self, node, result):
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)

    def display(self):
        result = []
        self.in_order_traversal(self.root, result)
        print("In-order Traversal:", result)

# Example Usage
tree = BinaryTree()
values = [10, 5, 15, 2, 7, 12, 20]
for value in values:
    tree.insert(value)

tree.display()
