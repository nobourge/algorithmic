class Node:
    def __init__(self, item):
        self.info = item
        self.left = None
        self.right = None

    def getInfo(self):
        return self.info

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setInfo(self, newinfo):
        self.info = newinfo

    def setLeft(self, newleft):
        self.left = newleft

    def setRight(self, newright):
        self.right = newright


class BinaryTree:
    def __init__(self, item):
        self.root = Node(item)

    def getRoot(self):
        return self.root

    def modifyLeft(self, base, item):
        base.setLeft(Node(item))

    def modifyRight(self, base, item):
        base.setRight(Node(item))
