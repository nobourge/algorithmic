def preorder(tree):
    while tree:
        print tree.getRootVal()        
        preorder(tree.getLeftChild())
        tree = tree.getRightChild()  
