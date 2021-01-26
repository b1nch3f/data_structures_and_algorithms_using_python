class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree (Node):

    def insert(self, data):

        if data < self.data:

            if self.left is None:

                self.left = BinarySearchTree(data)

            else:

                self.left.insert(data)

        else:

            if self.right is None:

                self.right = BinarySearchTree(data)

            else:

                self.right.insert(data)
