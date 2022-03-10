def niveau(noeud):
	f=Queue()
	f.insert(noeud)
	while not f.isEmpty():
		n = f.remove()
		if n != None:
			print n.getInfo()
			f.insert(n.getLeft())
			f.insert(n.getRight())
