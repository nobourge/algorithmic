def inorder(noeud):
    while noeud != None:
        inorder(noeud.getLeft())
        print noeud.getInfo()
        noeud = noeud.getRight()
