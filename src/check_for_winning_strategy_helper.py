from check_for_winning_strategy import *
	
vertices_graph = {0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8}
edges_graph = { 0: [1,3] ,
				1: [0,2] , 
              	2: [1,5] , 
              	3: [4,6] , 
              	4: [0,7,8] , 
              	5: [1,7] , 
              	6: [7] , 
              	7: [8,6] , 
              	8: [5]  
              }

vertex_to_player = { 0: 1 ,	
					 1: 0 , 
					 2: 1 , 
					 3: 0 , 
					 4: 1 , 
					 5: 1 , 
					 6: 1 , 
					 7: 0 ,
					 8: 0 
					}

bad_states = {3 , 6 }

for initial_state in range(9):
	print( "For state v" + str(initial_state) + ": " + str(check_if_always_winning_stratergy( vertices_graph, edges_graph, vertex_to_player, bad_states , initial_state, 0)))

