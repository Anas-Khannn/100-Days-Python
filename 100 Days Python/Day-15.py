"""
An AVL Tree is a self-balancing Binary Search Tree (BST) named after its inventors, Adelson-Velsky and Landis. 
It ensures that the height difference (or balance factor) between the left and right subtrees of any node is at most 1, 
maintaining efficient operations like search, insertion, and deletion.

Key Properties:
Balance Factor:

For every node, the balance factor is the height of the left subtree minus the height of the right subtree.
Balance Factor =
Height(left)

Height(right)
Balance Factor=Height(left)−Height(right)
Must always be 
−
1
≤
Balance Factor
≤
1
−1≤Balance Factor≤1.
Height Balance:

This balancing ensures that the tree does not degenerate into a linked list, providing 
𝑂
(
log
⁡
𝑛
)
O(logn) time complexity for search, insertion, and deletion.
Rotations:

To maintain balance, AVL trees perform rotations during insertion and deletion:
Left Rotation (LL imbalance).
Right Rotation (RR imbalance).
Left-Right Rotation (LR imbalance).
Right-Left Rotation (RL imbalance).
Advantages:
Fast Operations:

Balanced height ensures logarithmic time complexity.
Ideal for scenarios where frequent insertions and deletions occur.
Consistent Performance:

Always maintains balance, unlike an ordinary BST, which may become skewed.







"""



















class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    def insert(self, node, key):
        # Perform normal BST insertion
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Update height of this ancestor node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Get the balance factor
        balance = self.get_balance(node)

        # Balance the tree
        # Case 1 - Left Left
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Case 2 - Right Right
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Case 3 - Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Case 4 - Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def pre_order(self, node):
        if not node:
            return
        print(node.key, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

# Example usage
if __name__ == "__main__":
    avl = AVLTree()
    root = None

    # Insert nodes
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = avl.insert(root, key)

    # Pre-order traversal
    print("Pre-order traversal of the constructed AVL tree:")
    avl.pre_order(root)
