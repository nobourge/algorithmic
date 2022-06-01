def inorder(tree):
    while tree != None:
        inorder(tree.getLeftChild())
        print tree.getRootVal()
        tree = tree.getRightChild()
