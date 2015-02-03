class Node:
	def __init__(self, item):
		self.data = item
		self.next = None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, item):
		self.data = item

	def set_next(self, new_next):
		self.next = new_next

class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp

	def size(self):
		current_node = self.head
		count = 0
		while current_node != None:
			count += 1
			current_node = current_node.get_next()
		return count

	def search(self, item):
		current_node = self.head
		found = False
		while current_node != None and not found:
			if current_node.get_data() == item:
				found = True
			else:
				current_node = current_node.get_next()
		return found

	def remove(self, item):
		current_node = self.head
		prev_node = None
		found = False
		while not found:
			if current_node.get_data() == item:
				found = True
			else:
				prev_node = current_node
				current_node = current_node.get_next()
		if prev_node == None:
			self.head = current_node.get_next()
		else:
			prev_node.set_next(current_node.get_next())

#mylist = UnorderedList()

#mylist.add(31)
#mylist.add(77)
#mylist.add(17)
#mylist.add(93)
#mylist.add(26)
#mylist.add(54)

#print(mylist.size())
#print(mylist.search(93))
#print(mylist.search(100))

#mylist.add(100)
#print(mylist.search(100))
#print(mylist.size())

#mylist.remove(54)
#print(mylist.size())
#mylist.remove(93)
#print(mylist.size())
#mylist.remove(31)
#print(mylist.size())
#print(mylist.search(93))