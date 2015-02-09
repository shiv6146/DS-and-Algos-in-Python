import sys
sys.path.append('/home/shiva/Documents/shiv/pythonds/')
from stack import Stack
from binary_tree import BinaryTree
import operator

def build_parse_tree(expressionString):
	exp_list = expressionString.split()
	parent_stack = Stack()
	exp_tree = BinaryTree('')
	parent_stack.push(exp_tree)
	current_tree = exp_tree

	for token in exp_list:
		if token == '(':
			current_tree.insert_left('')
			parent_stack.push(current_tree)
			current_tree = current_tree.get_left_child()
		elif token not in ['*', '/', '+', '-', ')']:
			current_tree.set_root_val(int(token))
			parent = parent_stack.pop()
			current_tree = parent
		elif token in ['*', '/', '+', '-']:
			current_tree.set_root_val(token)
			current_tree.insert_right('')
			parent_stack.push(current_tree)
			current_tree = current_tree.get_right_child()
		elif token == ')':
			current_tree = parent_stack.pop()
		else:
			raise ValueError

	return exp_tree

def evaluate_parse_tree(parseTreeRoot):
	operators = {'*':operator.mul, '/':operator.truediv, '+':operator.add, '-':operator.sub}
	left_child = parseTreeRoot.get_left_child()
	right_child = parseTreeRoot.get_right_child()

	if left_child and right_child:
		fn = operators[parseTreeRoot.get_root_val()]
		return fn(evaluate_parse_tree(left_child), evaluate_parse_tree(right_child))
	else:
		return parseTreeRoot.get_root_val()

#Application of preorder traversal
def preorder(tree):
	if tree:
		print tree.get_root_val()
		preorder(tree.get_left_child())
		preorder(tree.get_right_child())

#Application of inorder traversal
def print_exp(tree):
	exp = ""
	if tree:
		exp = "(" + print_exp(tree.get_left_child())
		exp += str(tree.get_root_val())
		exp += print_exp(tree.get_right_child()) + ")"
	return exp

#Application of postorder traversal
def postorder_eval(tree):
	operators = {"*":operator.mul, "/":operator.truediv, "+":operator.add, "-":operator.sub}

	res1 = None
	res2 = None

	if tree:
		res1 = postorder_eval(tree.get_left_child())
		res2 = postorder_eval(tree.get_right_child())

		if res1 and res2:
			fn = operators[tree.get_root_val()]
			return fn(res1, res2)
		else:
			return tree.get_root_val()

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
#print evaluate_parse_tree(pt)
#preorder(pt)
#print print_exp(pt)
#print postorder_eval(pt)