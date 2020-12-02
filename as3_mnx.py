#Assignment 3
from as3_tree import Tree
class Result:
	def __init__(self, sol=[], val=-1000):
			self.solution = sol
			self.value = val

class MNX:
	def __init__(self, data_list):
		self.tree = Tree()
		self.tree.init_tree(data_list)
		self.root = self.tree.root
		self.currentNode = None
		self.successors = []
		return

	def terminalTest(self, node):
		assert node is not None
		return len(node.children) == 0

	def utilityChecking(self, node):
		assert node is not None
		return node.value

	def getChildren(self, node):
		assert node is not None
		return node.children

	def minimax(self):
		terminal_val = self.max_v(self.root)
		successors = self.getChildren(self.root)
		self.traversed = [self.root.Name]
		self.traverse(self.root, terminal_val)

		res = Result();
		res.value = terminal_val
		res.solution = self.traversed
		return res

	def max_v(self, node):
		if self.terminalTest(node):
			return self.utilityChecking(node)
		max_v =-1000   #we use 1000 as the initial_maximum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			max_v = max(max_v, self.min_v(deeper_node))
			self.gobytreetofindnode(deeper_node, max_v)
		return max_v

	def min_v(self, node):
		if self.terminalTest(node):
			return self.utilityChecking(node)
		min_v =1000  #we use -1000 as the initial_minimum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			min_v = min(min_v, self.max_v(deeper_node))
			self.gobytreetofindnode(deeper_node, min_v)
		return min_v

	def gobytreetofindnode(self, node, value): #to put tree in every node
		while node != self.tree.root:
			node.parent.value = value
			node = node.parent

	def traverse(self, node, value):  #traversing node to root
		child = self.getChildren(node)
		for noding in child:
			if noding.value == value:
				self.traversed.append(noding.Name)
				r = self.traverse(noding, value)
				return r