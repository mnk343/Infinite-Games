from copy import copy

# vertices_graph = {0 ,1,2,3,4,5,6,7,8}
# edges_graph = { 0: [1,3] ,1 : [0,2] , 
# 				2: [1,5] , 3: [4,6] , 4: [0,7,8] , 5:[1,7] , 
# 				6:[7] , 7: [8,6] , 8:[5]  }
# map_vertex_to_player = { 0: 1 ,1:0 , 2:1 , 3: 0 , 4: 1 , 5:0 , 6: 1 , 7:0 ,8:0 }

if __name__ == "__main__":
    vertices_graph = {0,1,2,3,4}
    edges_graph = {
                    0: [1,4],
                    1: [0,2],
                    2: [1,3],
                    3: [3],
                    4: [2]
    }

    map_vertex_to_player = { 0:0 , 1:1, 2:0 , 3:1 , 4: 1}

    bad_states = [
        {2},
        {3}
    ]

    # for i in range(0,5):
    # 	initial_state = i
    # 	print(i, check_if_always_winning_stratergy( vertices_graph, edges_graph, map_vertex_to_player, bad_states , initial_state, 1))

    n = 0
    all_transitions = {}
    players = [0, 1]
    edges_graph_with_removed_transitions = copy(edges_graph)

    # player_index = 0
    # vertex = 1
    # print("mayansk")
    # print(check_if_never_winning_stratergy(vertices_graph, edges_graph_with_removed_transitions, map_vertex_to_player, bad_states[player_index], vertex, player_index))
    # print(check_if_always_winning_stratergy(vertices_graph, edges_graph_with_removed_transitions, map_vertex_to_player, bad_states[player_index], vertex, player_index))

    while True:
        value = {}
        for vertex in vertices_graph:
            for player_index in players:
                if not check_if_never_winning_stratergy(vertices_graph, edges_graph_with_removed_transitions, map_vertex_to_player, bad_states[player_index], vertex, player_index) == True:
                    value[player_index, vertex] = 0
                elif check_if_never_winning_stratergy(vertices_graph, edges_graph_with_removed_transitions, map_vertex_to_player, bad_states[player_index], vertex, player_index) == True:
                    value[player_index, vertex] = -1
                else:
                    value[player_index, vertex] = 1
        

        transitions_old_count = len(all_transitions)

        for player_index in players:
            for vertex, adjacent_vertices in edges_graph.items():
                if vertex in map_vertex_to_player and map_vertex_to_player[vertex] == player_index:
                    for adj_vertex in adjacent_vertices:
                        if (player_index, vertex, adj_vertex) not in all_transitions:
                            if value[player_index, vertex] > value[player_index, adj_vertex]:
                                all_transitions[(player_index, vertex, adj_vertex)] = 1
                                if adj_vertex in edges_graph_with_removed_transitions[vertex]:
                                    edges_graph_with_removed_transitions[vertex].remove(adj_vertex)

        transitions_new_count = len(all_transitions)

        if transitions_new_count == transitions_old_count:
            break

    for t in all_transitions:
        print(t[1], t[2])
