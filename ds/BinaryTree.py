class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, data):
        self.head = Tree(data)

    def insertLeft(self, data):
        self.head.left = Tree(data)

    def insertRight(self, data):
        self.head.right = Tree(data)

    def getData(self):
        return self.head.data
