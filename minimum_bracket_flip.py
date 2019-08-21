class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	# Returns top value of the stack which we need to solve the below problem
	# a feature which doesn't come with default python
	def peek(self):	
		if len(self.items) == 0:
			return ''
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

	def show(self):
		return self.items

	
def count_min_reverse(expr):
	expr_len = len(expr)

	if (expr_len % 2):
		return 'Can\'t Be balanced'

	stack = Stack()

	for i in range(expr_len):
		if expr[i] == '}' and stack.peek() == "{":
			stack.pop()
		else:
			stack.push(expr[i])

	reduced_len = stack.size()

	n = 0
	for i in stack.items:
		if i == '{':
			n += 1

	print(stack.show())
	return (reduced_len / 2 + n % 2)

print(count_min_reverse('{{{'))