from copy import copy
# edges_graph is in adjacency matrix format

def find_winning_region_reachability_game(vertices_graph, edges_graph, map_vertex_to_player, good_states):
	attractor_i = copy(good_states)
	# print("h")
	updated_length = len(good_states)
	prev_length = len(good_states)-1

	while prev_length != updated_length:
		prev_length = len(attractor_i)
		c_pre_i = set()
		#Find Controlled Predecessor
		for vertex in vertices_graph:
			if vertex in attractor_i:
				continue
			if map_vertex_to_player[vertex] == 0:
				flag = 0
				for successor in edges_graph[vertex]:
					if successor in attractor_i:
						flag = 1
						break
			else:
				flag = 1
				for successor in edges_graph[vertex]:
					if successor not in attractor_i:
						flag = 0
						break
			if flag == 1:
				c_pre_i.add(vertex)

		for vertex in c_pre_i:
			attractor_i.add(vertex)

		updated_length = len(attractor_i)

	return attractor_i

def check_if_always_winning_stratergy( vertices_graph, edges_graph, vertex_to_player, bad_states , initial_state, player_index):
	map_vertex_to_player = copy(vertex_to_player)
	if player_index == 1:
		for key,value in map_vertex_to_player.items():
			map_vertex_to_player[key] = (value+1)%2

	dual_map_vertex_to_player = {}
	good_states = bad_states
	for vertex in vertices_graph:
		dual_map_vertex_to_player[vertex] = (map_vertex_to_player[vertex] + 1 ) % 2

	winning_region = find_winning_region_reachability_game(vertices_graph, edges_graph, dual_map_vertex_to_player, good_states)
	if initial_state not in winning_region: 
		# print("True")
		return True
	return False

def check_if_never_winning_stratergy( vertices_graph, edges_graph, vertex_to_player, bad_states , initial_state, player_index):
	map_vertex_to_player = copy(vertex_to_player)
	for key,value in map_vertex_to_player.items():
		map_vertex_to_player[key] = 0

	dual_map_vertex_to_player = {}
	good_states = bad_states
	for node in vertices_graph:
		dual_map_vertex_to_player[node] = (map_vertex_to_player[node] + 1 ) % 2

	winning_region = find_winning_region_reachability_game(vertices_graph, edges_graph, dual_map_vertex_to_player, good_states)
	if initial_state not in winning_region: 
		return False
	return True

# vertices_graph = {0 ,1,2,3,4,5,6,7,8}
# edges_graph = { 0: [1,3] ,1 : [0,2] , 
# 				2: [1,5] , 3: [4,6] , 4: [0,7,8] , 5:[1,7] , 
# 				6:[7] , 7: [8,6] , 8:[5]  }
# map_vertex_to_player = { 0: 1 ,1:0 , 2:1 , 3: 0 , 4: 1 , 5:0 , 6: 1 , 7:0 ,8:0 }

# vertices_graph = {0,1,2,3,4}
# edges_graph = {
# 				0: [1,4],
# 				1: [0,2],
# 				2: [1,3],
# 				3: [3],
# 				4: [2]
# }

# map_vertex_to_player = { 0:0 , 1:1, 2:0 , 3:1 , 4: 0}

# bad_states = {3}

# for i in range(0,5):
# 	initial_state = i
# 	print(i, check_if_always_winning_stratergy( vertices_graph, edges_graph, map_vertex_to_player, bad_states , initial_state, 1))
