from copy import copy
# edges_graph is in adjacency matrix format

def find_winning_region_reachability_game(vertices_graph, edges_graph, map_vertex_to_player, good_states):
	attractor_i = copy(good_states)
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
	