def preorder(noeud):
    while noeud:
        print noeud.getInfo()        
        preorder(noeud.getLeft())
        noeud = noeud.getRight()  
