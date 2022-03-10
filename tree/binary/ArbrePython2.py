class BinaryTree:
	def __init__(self,item):
		self.info = item
		self.left = None
		self.right = None
	
	def modifyLeft(self,item):
		self.left = BinaryTree(item)
	
	def modifyRight(self,item):
		self.right = BinaryTree(item)
	
	def getRootVal(self):
		return self.info
	
	def setRootVal(self,item):
		self.info = item
	
	def getLeftChild(self):
		return self.left
	
	def getRightChild(self):
		return self.right
			
	