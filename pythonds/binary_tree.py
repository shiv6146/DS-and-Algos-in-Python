class BinaryTree:
	def __init__(self, newNodeVal):
		self.rootval = newNodeVal
		self.left_child = None
		self.right_child = None

	def insert_left(self, newNodeVal):
		if self.left_child == None:
			self.left_child = BinaryTree(newNodeVal)
		else:
			temp = BinaryTree(newNodeVal)
			temp.left_child = self.left_child
			self.left_child = temp

	def insert_right(self, newNodeVal):
		if self.right_child == None:
			self.right_child = BinaryTree(newNodeVal)
		else:
			temp = BinaryTree(newNodeVal)
			temp.right_child = self.right_child
			self.right_child = temp

	def get_root_val(self):
		return self.rootval

	def get_left_child(self):
		return self.left_child

	def get_right_child(self):
		return self.right_child

	def set_root_val(self, newNodeVal):
		self.rootval = newNodeVal

	def preorder(self):
		print self.rootval
		if self.left_child:
			return self.left_child.preorder()
		if self.right_child:
			return self.right_child.preorder()

	def inorder(self):
		if self.left_child:
			return self.left_child.inorder()
		print self.rootval
		if self.right_child:
			return self.right_child.inorder()

	def postorder(self):
		if self.left_child:
			return self.left_child.postorder()
		if self.right_child:
			return self.right_child.postorder()
		print self.rootval