def BinaryTree(r):
	return [r, [], []]

def insert_left(root, new_branch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [new_branch, t, []])
	else:
		root.insert(1, [new_branch, [], []])
	return root

def insert_right(root, new_branch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [new_branch, t, []])
	else:
		root.insert(2, [new_branch, [], []])

def get_root_val(root):
	return root[0]

def get_right_child(root):
	return root[1]

def get_left_child(root):
	return root[2]


x = BinaryTree('a')
insert_left(x,'b')
insert_right(x,'c')
insert_right(get_right_child(x),'d')
insert_left(get_right_child(get_right_child(x)),'e')
