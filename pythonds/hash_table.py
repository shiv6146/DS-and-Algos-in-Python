class HashTable:
	def __init__(self, size):
		self.size = size
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self, key, value):
		hash_value = self.hash_function(key, len(self.slots))

		if self.slots[hash_value] == None:
			self.slots[hash_value] = key
			self.data[hash_value] = value
		else:
			if self.slots[hash_value] == key:
				self.data[hash_value] = value   #replace the older value for the key
			else:
				next_slot = self.rehash_function(hash_value, len(self.slots))

				while self.slots[next_slot] != None and self.slots[next_slot] != key:
					next_slot = self.rehash_function(next_slot, len(self.slots))

				if self.slots[next_slot] == None:
					self.slots[next_slot] = key
					self.data[next_slot] = value
				else:
					self.data[next_slot] = value   #replace the older value of the key within the cluster

	def hash_function(self, key, size):
		return key%size

	def rehash_function(self, oldhash, size):
		return (oldhash+1)%size

	def get(self, key):
		startslot = self.hash_function(key, len(self.slots))

		found = False
		data = None
		stop = False
		pos = startslot

		while self.slots[pos] != None and not found and not stop:
			if self.slots[pos] == key:
				found = True
				data = self.data[pos]
			else:
				pos = self.rehash_function(pos, len(self.slots))
				if pos == startslot:
					stop = True
		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		return self.put(key, value)
