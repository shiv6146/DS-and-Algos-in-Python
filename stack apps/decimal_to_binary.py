import sys
sys.path.append('/home/shiva/Documents/shiv/pythonds/')
from stack import Stack

def decimal_to_binary(decimal):
	s = Stack()
	binary = ""
	while decimal > 0:
		s.push(decimal%2)
		decimal/=2
	while not s.isEmpty():
		binary += str(s.pop())
	return binary

print decimal_to_binary(42)
print decimal_to_binary(4)
print decimal_to_binary(5)