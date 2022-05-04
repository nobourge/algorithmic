def BinaryTree(r):
    return [r, [], []]


def modifyLeft(root, value):
    """
	:param root:
	:param value:
	:return:
	"""
    t = root.pop(1)
    root.insert(1, [value, [], []])
    return root


def modifyRight(root, value):
    t = root.pop(2)
    root.insert(2, [value, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]
