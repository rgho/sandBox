# STORE THE GRAPH
adjacencies = dict()
adjacencies[1] = [2,4]
adjacencies[2] = [1,3,5]
adjacencies[3] = [2]
adjacencies[4] = [1,7]
adjacencies[5] = [6,8,2]
adjacencies[6] = [5,9,10]
adjacencies[7] = [4]
adjacencies[8] = [5]
adjacencies[9] = [6,12]
adjacencies[10] = [6,11]
adjacencies[11] = [10]
adjacencies[12] = [9]

# store second graph
adjacencies2 = dict()
adjacencies2[1] = [2,4]
adjacencies2[2] = [1,3,5]
adjacencies2[3] = [2,11]
adjacencies2[4] = [1,5,7]
adjacencies2[5] = [6,8,2,4]
adjacencies2[6] = [5,9,10]
adjacencies2[7] = [4,13]
adjacencies2[8] = [5,14]
adjacencies2[9] = [6,12]
adjacencies2[10] = [6,11]
adjacencies2[11] = [3,10]
adjacencies2[12] = [9]
adjacencies2[13] = [7,14]
adjacencies2[14] = [13,8]
adjacencies2[15] = [16]
adjacencies2[16] = [15]

def find_path(destination,graph,current_path,already_visited):
	# depth first.
	# WE CONTINUE LOOPING WHILE WE HAVE NOT REACHED DEST OR WHILE PATH IS NOT EMPTY
	while (current_path[-1] != destination and len(current_path)!=0):
		
		# WE ASSIGN A VALUE FOR CURRENT NODE BASED ON THE L:AST ITEM IN PATH
		current_node = current_path[-1]
		# GET NODES WE CAN POSSIBLY GO TO FROM CURRENT NODE
		available_nodes =  graph[current_node]
		print "current_node: " +str(current_node)
		print "vis:" + str(already_visited)
		print "available nodes: " + str(available_nodes)
		print  "path: " + str(current_path)

		# FOR EACH AVAILABLE NODE FOR A CURRENT NODE, WE DO THE FOLLOWING
		for available_node in available_nodes:
		# STILL ON ONE
			if available_node in already_visited:
				print "already been to, removing: " +  str(available_node)
				available_nodes.remove(available_node)
		
		if len(available_nodes) > 0:
			# STILL HAE SOMEWHERE TO Go			
			# decide what the next node is
			current_node = available_nodes[0]
			current_path.append(current_node)
			already_visited.append(current_node)
			print "going to : " + str(current_node)
			#pdb.set_trace()
			print
		else:
			print "popped: " +str(current_path[-1])
			current_path.pop()
			current_node = current_path[-1]
	# WHEN WHILE LOOP IS DONE WE HAVE THE ANSWER, IT MAYBE EMPTY (NO CONENECT) 
	return current_path
#print find_path(10,adjacencies,[1],[1])


def connected_to(node,graph):
	return graph[node]

def graph_breadth_search(start,destination,graph):
	# some inits
	current_nodes = [start]
	already_visited = [start]
	path_list = [[start]] # is never used in any core logic. #can remove all path code and
	#this will still test for existance of a shortest path between two points.
	#print path_list
	while len(current_nodes) > 0:
		# operate on the first in list
		current_node = current_nodes[0]
		# also grab the corresponding path
		current_path = path_list[0]
		#get list of nodes connected to current node
		nodes_connected_to_current_node = connected_to(current_node,graph)
		#remove nodes that have already been visited.
		nodes_connected_to_current_node = list(set(nodes_connected_to_current_node) - set(already_visited))
		#check if node_connected is empty prob not needed
		for node in nodes_connected_to_current_node:
			if node == destination:
				current_path.append(node)
				return "first shortest path found: " + str(current_path)
				break #needed?
			else:
				#this is the case when unvisited, non destination nodes are connected
				#to the current_node. we add them to the visited list and current nodes.
				current_nodes.append(node)
				already_visited.append(node)
				# 3 lines to deal with adding paths to list
				temp = list(current_path) # this is a critical line. 
				#something like temp = current_path does not actualy copy the list and cuases toruble.
				temp.append(node)
				path_list.append(temp)

		#remove the current node (first item) from the current 
		#nodes, making current nodes act like a queue.
		current_nodes = current_nodes[1:]
		path_list = path_list[1:]
	#if we have exited the while loop then no connections were found!
	return "no connection found."
print graph_breadth_search(1,12,adjacencies2)





























