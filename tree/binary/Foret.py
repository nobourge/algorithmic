class Foret:
	def __init__(self,item):
		self.info = item
		self.child = None
		self.brother = None
	
	def getRootVal(self,):
		return self.info
	
	def setRootVal(self,item):
		self.info = item
	
	def getChild(self):
		return self.child
	
	def getBrother(self):
		return self.brother
	
	def modifyChild(self,newNode):
		self.child = Foret(newNode)
	
	def modifyBrother(self,newNode):
		self.brother = Foret(newNode)
	