import sys
sys.path.append('/home/shiva/Documents/shiv/pythonds/')
import string
from stack import Stack

def postfix_evaluation(postfixString):
	operand_stack = Stack()
	token_list = postfixString.split()

	for token in token_list:
		if token in string.digits:
			operand_stack.push(int(token))
		else:
			second = operand_stack.pop()
			first = operand_stack.pop()
			operand_stack.push(do_calc(first, second, token))
	return operand_stack.pop()

def do_calc(first, second, operator):
	if operator == '*':
		return first * second
	elif operator == '/':
		return first / second
	elif operator == '+':
		return first + second
	elif operator == '-':
		return first - second
	else:
		return 'valid operator'

print postfix_evaluation('7 8 + 3 2 + /')