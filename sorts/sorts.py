class Sorts:
	def __init__(self, mylist=None):
		self.mylist = mylist

	def bubble_sort(self):
		for passnum in range(len(self.mylist)-1, 0, -1):
			for i in range(passnum):
				if self.mylist[i] > self.mylist[i+1]:
					self.mylist[i], self.mylist[i+1] = self.mylist[i+1], self.mylist[i]

	def optimized_bubble_sort(self):
		exchanges = True
		passnum = len(self.mylist)-1

		while passnum > 0 and exchanges:
			exchanges = False
			for i in range(passnum):
				if self.mylist[i] > self.mylist[i+1]:
					exchanges = True
					self.mylist[i], self.mylist[i+1] = self.mylist[i+1], self.mylist[i]
			passnum -= 1

	def selection_sort(self):
		for slot in range(len(self.mylist)-1, 0, -1):
			max_pos = 0
			for i in range(1, slot+1):
				if self.mylist[i] > self.mylist[max_pos]:
					max_pos = i
			self.mylist[slot], self.mylist[max_pos] = self.mylist[max_pos], self.mylist[slot]

	def insertion_sort(self):
		for i in range(1, len(self.mylist)):
			cur_val = self.mylist[i]
			pos = i
			while pos > 0 and self.mylist[pos-1] > cur_val:
				self.mylist[pos] = self.mylist[pos-1]
				pos -= 1
			self.mylist[pos] = cur_val

	def shell_sort(self):
		sub_list_count = len(self.mylist) // 2
		while sub_list_count > 0:
			for start_pos in range(sub_list_count):
				self.helper_shell_sort(start_pos, sub_list_count)
			sub_list_count = sub_list_count // 2

	def helper_shell_sort(self, start, gap):
		for i in range(start+gap, len(self.mylist), gap):
			cur_val = self.mylist[i]
			pos = i
			while pos >= gap and self.mylist[pos-gap] > cur_val:
				self.mylist[pos] = self.mylist[pos-gap]
				pos = pos - gap
			self.mylist[pos] = cur_val

	def merge_sort(self, mylist):
		if len(mylist) > 1:
			mid = len(mylist) // 2
			left_half = mylist[:mid]
			right_half = mylist[mid:]
			self.merge_sort(left_half)
			self.merge_sort(right_half)
			i=0
			j=0
			k=0
			while i < len(left_half) and j < len(right_half):
				if left_half[i] < right_half[j]:
					mylist[k] = left_half[i]
					i += 1
				else:
					mylist[k] = right_half[j]
					j += 1
				k += 1
			while i < len(left_half):
				mylist[k] = left_half[i]
				i += 1
				k += 1
			while j < len(right_half):
				mylist[k] = right_half[j]
				j += 1
				k += 1
		return mylist

	def quick_sort(self):
		self.quick_sort_helper(0, len(self.mylist)-1)

	def quick_sort_helper(self, first, last):
		if first < last:
			split_point = self.partition(first, last)
			self.quick_sort_helper(first, split_point-1)
			self.quick_sort_helper(split_point+1, last)

	def partition(self, first, last):
		pivot = self.mylist[first]
		left_mark = first + 1
		right_mark = last
		done = False
		while not done:
			while left_mark <= right_mark and self.mylist[left_mark] <= pivot:
				left_mark += 1
			while self.mylist[right_mark] >= pivot and right_mark >= left_mark:
				right_mark -= 1
			if right_mark < left_mark:
				done = True
			else:
				self.mylist[left_mark], self.mylist[right_mark] = self.mylist[right_mark], self.mylist[left_mark]
		self.mylist[first], self.mylist[right_mark] = self.mylist[right_mark], self.mylist[first]
		return right_mark