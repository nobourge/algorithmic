def postorder(noeud):
    if noeud != None:
        postorder(noeud.getLeft())
        postorder(noeud.getRight())
        print noeud.getInfo()        
