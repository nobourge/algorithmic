def preordre(forest):
	while forest != None:
		print forest.getRootVal()
		preorder(forest.getChild())
		forest = forest.getBrother()

def postorder(forest):
	while forest != None:
		postorder(forest.getChild())
		print forest.getRootVal()
		forest = forest.getBrother()

def niveau(forest):
	f=Queue()
	f.insert(forest)
	while not f.isEmpty():
		n = f.remove()
		while n != None:
			print n.getRootVal()
			f.insert(n.getChild())
			n = n.getBrother())
