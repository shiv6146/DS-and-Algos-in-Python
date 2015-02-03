import sys
sys.path.append('/home/shiva/Documents/shiv/pythonds/')
import string
from stack import Stack

def infix_to_postfix(infixString):
	op_precedence = {}
	op_precedence["*"] = 3
	op_precedence["/"] = 3
	op_precedence["+"] = 2
	op_precedence["-"] = 2
	op_precedence["("] = 1

	postfix_list = []
	opstack = Stack()
	token_list = infixString.split()

	for token in token_list:
		if token in string.ascii_uppercase or token in string.digits:
			postfix_list.append(token)
		elif token == '(':
			opstack.push(token)
		elif token == ')':
			top_token = opstack.pop()
			while top_token != '(':
				postfix_list.append(top_token)
				top_token = opstack.pop()
		else:
			while (not opstack.isEmpty()) and (op_precedence[opstack.peek()] >= op_precedence[token]):
				postfix_list.append(opstack.pop())
			opstack.push(token)

	while not opstack.isEmpty():
		postfix_list.append(opstack.pop())

	return ' '.join(postfix_list)

print infix_to_postfix("A * B + C * D")
print infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )")