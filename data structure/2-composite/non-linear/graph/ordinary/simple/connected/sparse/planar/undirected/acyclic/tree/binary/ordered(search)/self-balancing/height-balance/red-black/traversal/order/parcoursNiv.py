def niveau(tree):
	f=Queue()
	f.insert(tree)
	while not f.isEmpty():
		n = f.remove()
		if n != None:
			print n.getRootVal()
			f.insert(n.getLeftChild())
			f.insert(n.getRightChild())
