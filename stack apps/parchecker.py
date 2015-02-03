import sys
sys.path.append('/home/shiva/Documents/shiv/pythonds')
from stack import Stack

def parchecker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == '(':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		index+=1

	if s.isEmpty() and balanced:
		return True
	else:
		return False

print parchecker('((()))')
print parchecker('(((((((((()))')
