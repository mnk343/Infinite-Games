import pickle

good_transitions = pickle.load( open ( "good_transitions4" , "rb"))
all_transitions = pickle.load( open ( "all_transitions4" , "rb"))

time_bound = 4
vertices_graph = set()
state_index = 1
map_index_to_state = {}
map_vertex_to_player = {}
map_state_to_index = {}
edges_graph = {}

for a1 in range(2):
    for a2 in range(2):
        for r1 in range(2):
            for r2 in range(2):
                for k1 in range(time_bound):
                    for k2 in range(time_bound):
                        for q1 in range(2):
                            for q2 in range(2):
                                for t1 in range(3):
                                    for t2 in range(3):
                                        for p in range(3):
                                            temp_state = (a1, a2, r1, r2, k1, k2, q1, q2, t1, t2, p)
                                            vertices_graph.add(state_index)
                                            map_state_to_index[temp_state] = state_index
                                            map_index_to_state[state_index] = temp_state
                                            map_vertex_to_player[ state_index ] = p 
                                            state_index += 1

for t in vertices_graph:
	edges_graph[ t ] = []

for t in good_transitions:
	edges_graph[ t[1] ].append( t[2] )


bad_state_index = state_index
map_index_to_state[state_index] = (-1)

vertices_graph.add(bad_state_index)
map_vertex_to_player[ state_index ] = 0

bad_states = [
    {bad_state_index}, 
    {bad_state_index}, 
    {bad_state_index}
]

start_state = (1,1, 0,0, time_bound-1, time_bound-1, 0, 0 , 2, 2, 0)
start_state_index = map_state_to_index[ start_state ]
while 1:
	print(start_state_index)
	print(map_index_to_state[start_state_index])
	print( edges_graph[start_state_index] ) 
	print("")

	if len(edges_graph[start_state_index]) == 0:
		print("DONE")
		break
	if start_state_index == bad_state_index:
		print("END")
		break

	start_state = map_index_to_state[start_state_index]
	if start_state[ 0 ] + start_state[1] + start_state[ 2 ] + start_state[ 3 ] + start_state[ 6 ] + start_state[ 7 ] is 0:
		print ("ALL PACKETS SENT")
		break

	start_state_index = edges_graph[start_state_index][0]
