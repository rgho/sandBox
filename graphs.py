import pdb


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

def remove_matching_items(target_list,match_elements):
	for item in target_list:
		if item in match_elements:
			target_list.remove(item)
	return target_list
#if dead end try aniother, add to visited lis 


def find_path(destination,graph,current_path,already_visited):
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




def find_shortest_path_breadth(start, desitnation, graph):
	#init
	nearby_nodes = [start]
	paths_for_existing_nodes = []
	current = start

	while True:
		## HAPPENS MANY TIMES
		nodes = nodesOf[current]
		if destination in nodes:
			#shortest found
			return paths_for_existing_nodes[thisNode] + destination
		else:
			untraversed_nodes = diff(nodes,visited)
			# add to end
			nearby_nodes.append(untraversed_nodes)
			paths_for_existing_nodes.append(path_till_now + untraversed_nodes)
			# remove from front
			nearby_nodes.pop(current)
			paths_for_existing_nodes.pop(current)
		break

print find_shortest_path_breadth(1, 10, adjacencies)






























