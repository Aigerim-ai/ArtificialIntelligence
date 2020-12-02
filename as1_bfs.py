#Author: Dinh-Mao Bui, Anh-Tu Nguyen
#Rule of traversing: Alphabetical ordered, then left to right, 
#Points: 2
def traverse(tree, init):  # tree to travesrse, initial state  	
	queue = [init]
	traversed = [] 
	while queue:
		node = queue.pop(0)#pop first node from queue
		if node not in traversed:
			traversed.append(node)
			leaves = tree[node]
			for leaf in leaves: 
				queue.append(leaf)
	return traversed







#Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [[init]]
	if init == goal:
		return "No kidding, pls"
	while queue:
		node=queue.pop(0)
		top=node[-1]
		if top==goal:
			return node
		elif top not in traversed:
			for curr in tree.get(top,[]):
				new_node=list(node)
				new_node.append(curr)
				queue.append(new_node)
			traversed.append(top)

	while queue:					
		if(traversed[len(traversed)]!=goal):		
			break
			return "No such path exists"
		else:
			return traversed

 
