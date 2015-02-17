def binary_search(mylist, element):
	if len(mylist) == 0:
		return False
	else:
		mid = len(mylist) // 2
		if element == mylist[mid]:
			return True
		else:
			if element < mylist[mid]:
				return binary_search(mylist[:mid], element)
			else:
				return binary_search(mylist[mid+1:], element)