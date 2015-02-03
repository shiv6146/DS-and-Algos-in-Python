import sys
sys.path.append('/home/shiva/Documents/shiv/pythonds/')
from stack import Stack

def symbolchecker(symbolString):
	s = Stack()
	balanced = True
	index = 0

	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol in '({[':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top,symbol):
					balanced = False
		index+=1
	if s.isEmpty() and balanced:
		return True
	else:
		return False

def matches(open, close):
	openers = '({['
	closers = ')}]'
	return openers.index(open) == closers.index(close)

print symbolchecker('{{([][])}()}')
print symbolchecker('[{()]')