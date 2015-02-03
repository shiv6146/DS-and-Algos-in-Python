import sys
sys.path.append('/home/shiva/Documents/shiv/pythonds/')
from stack import Stack

def baseConverter(decimal, base):
	s = Stack()
	digits = "0123456789ABCDEF"
	numString = ""

	while decimal > 0:
		s.push(decimal%base)
		decimal/=base

	while not s.isEmpty():
		numString += digits[s.pop()]
	return numString

print baseConverter(25, 2)
print baseConverter(25, 8)
print baseConverter(25, 16)
