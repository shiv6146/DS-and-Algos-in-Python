class BinaryHeap:
	def __init__(self):
		self.heap_list = [0]
		self.current_size = 0

	def is_empty(self):
		if self.current_size:
			return False
		else:
			return True

	def size(self):
		return self.current_size

	def perc_up(self, i):  #Helper function for inserting a new node to maintain the binary heap property
		while i // 2 > 0:
			if self.heap_list[i] < self.heap_list[i//2]:
				self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
			i = i // 2

	def insert(self, k):
		self.heap_list.append(k)
		self.current_size += 1
		self.perc_up(self.current_size)


	def find_min(self):
		if self.current_size > 0:
			return self.heap_list[1]

	def min_child(self, i):
		if (i*2)+1 > self.current_size:      #Special case which checks for the completeness of the binary tree
			return i*2
		if self.heap_list[i*2] > self.heap_list[(i*2)+1]:  #Check for the smaller of the two children
			return (i*2)+1
		else:
			return i*2

	def perc_down(self, i):    #Helper function to delete the min node and maintain the binary heap property
		while (i*2) <= self.current_size:
			mc = self.min_child(i)
			if self.heap_list[i] > self.heap_list[mc]:
				self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
			i = mc

	def del_min(self):
		min_val = self.heap_list[1]
		self.heap_list[1] = self.heap_list[self.current_size]
		self.current_size -= 1
		self.heap_list.pop()
		self.perc_down(1)
		return min_val

	def build_heap(self, mylist):
		i = len(mylist) // 2       #Start from the mid element taking advantage of log property of complete binary tree
		self.current_size = len(mylist)
		self.heap_list = [0] + mylist
		while i > 0:
			self.perc_down(i)     #Rearrange the nodes to satisfy the binary heap property
			i -= 1
