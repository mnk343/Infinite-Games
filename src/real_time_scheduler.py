from copy import copy
from check_for_winning_strategy import *

if __name__ == "__main__":

    vertices_graph = {1,2,3}
    edges_graph = {
                    1: [2,3],
                    2: [1,3],
                    3: [3],
    }

    map_vertex_to_player = { 1:0, 2:1 , 3:0}

    bad_states = [
        {3},
        {3}
    ]


    # state = (a1, a2, r1, r2, k1, k2, q1, q2, t1, t2, p)

    vertices_graph = {}
    state_index = 1
    map_index_to_state = {}
    map_state_to_index = {}
    edges_graph = {}

    for a1 in range(1):
        for a2 in range(1):
            for r1 in range(1):
                for r2 in range(1):
                    for k1 in range(time_bound):
                        for k2 in range(time_bound):
                            for q1 in range(1):
                                for q2 in range(1):
                                    for t1 in range(1):
                                        for t2 in range(1):
                                            for p in range(3):
                                                temp_state = (a1, a2, r1, r2, k1, k2, q1, q2, t1, t2, p)
                                                vertices_graph.add(state_index)
                                                map_state_to_index[temp_state] = state_index
                                                map_index_to_state[state_index] = temp_index
                                                state_index += 1
                                                map_vertex_to_player[ temp_state ] = p 
                                                edges_graph[state_index] = []

    bad_state_index = state_index
    vertices_graph.add(bad_state_index)

    bad_states = [
        {bad_state_index}, 
        {bad_state_index}, 
        {bad_state_index}
    ]



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
                                                # if r1 == 0 and t1 != 2:
                                                curr_state = (a1, a2, r1, r2, k1, k2, q1, q2, t1, t2, p)
                                                curr_state_index = map_state_to_index[curr_state]

                                                if p == 0:
                                                    next_state = (a1, a2, r1, r2, k1, k2, 0, 0, t1, t2, (p+1)%3 )
                                                    next_state_index = map_state_to_index[next_state]
                                                    edges_graph[curr_state_index].append(next_state_index)

                                                elif p == 1:
                                                    if a1 is 0:
                                                        next_state = (a1, a2, r1, r2, k1, k2, q1, q2, t1, t2, (p+1)%3 )
                                                        next_state_index = map_state_to_index[next_state]
                                                        edges_graph[curr_state_index].append(next_state_index)
    
                                                    if a1 == 1 and r1 is 0:
                                                        if k1 is 1:
                                                            next_state_index = bad_state_index
                                                            edges_graph[curr_state_index].append(next_state_index)

                                                        else:
                                                            next_state = (1, a2, 0, r2, k1-1, k2, q1, q2, t1, t2, (p+1)%3 )
                                                            next_state_index = map_state_to_index[next_state]
                                                            edges_graph[curr_state_index].append(next_state_index)

                                                            next_state = (0, a2, 1, r2, k1-1, k2, q1, q2, 2, t2, (p+1)%3 )
                                                            next_state_index = map_state_to_index[next_state]
                                                            edges_graph[curr_state_index].append(next_state_index)

                                                    if a1 == 1 and r1 is 1:
                                                        if k1 is 1:
                                                            next_state = bad_state_index
                                                            edges_graph[curr_state_index].append(next_state_index)

                                                        else:
                                                            next_state = (a1, a2, r1, r2, k1-1, k2, q1, q2, t1, t2, (p+1)%3 )
                                                            next_state_index = map_state_to_index[next_state]
                                                            edges_graph[curr_state_index].append(next_state_index)


                                                    if a2 is 0:
                                                        next_state = (a1, a2, r1, r2, k1, k2, q1, q2, t1, t2, (p+1)%3 )
                                                        next_state_index = map_state_to_index[next_state]
                                                        edges_graph[curr_state_index].append(next_state_index)
    
                                                    if a2 == 1 and r2 is 0:
                                                        if k2 is 1:
                                                            next_state_index = bad_state_index
                                                            edges_graph[curr_state_index].append(next_state_index)

                                                        else:
                                                            next_state = (a1, 1, r1, 0, k1, k2-1, q1, q2, t1, t2, (p+1)%3 )
                                                            next_state_index = map_state_to_index[next_state]
                                                            edges_graph[curr_state_index].append(next_state_index)

                                                            next_state = (a1, 0, r1, 1, k1, k2-1, q1, q2, t1, 2, (p+1)%3 )
                                                            next_state_index = map_state_to_index[next_state]
                                                            edges_graph[curr_state_index].append(next_state_index)

                                                    if a2 == 1 and r2 is 1:
                                                        if k2 is 1:
                                                            next_state = bad_state_index
                                                            edges_graph[curr_state_index].append(next_state_index)
                                                            
                                                        else:
                                                            next_state = (a1, a2, r1, r2, k1, k2-1, q1, q2, t1, t2, (p+1)%3 )
                                                            next_state_index = map_state_to_index[next_state]
                                                            edges_graph[curr_state_index].append(next_state_index)
                                                
                                                else:
                                                    if r1 == 1:
                                                        if t1 == 0:
                                                            next_state = bad_state_index
                                                            edges_graph[curr_state_index].append(next_state_index)
                                                        else:
                                                            next_state = (a1, a2, r1, r2, k1, k2, q1, q2, t1-1, t2, (p+1)%3 )
                                                            next_state_index = map_state_to_index[next_state]
                                                            edges_graph[curr_state_index].append(next_state_index)
                                                        continue

                                                    if r2 == 1:
                                                        if t2 == 0:
                                                            next_state = bad_state_index
                                                            edges_graph[curr_state_index].append(next_state_index)
                                                        else:
                                                            next_state = (a1, a2, r1, r2, k1, k2, q1, q2, t1, t2-1, (p+1)%3 )
                                                            next_state_index = map_state_to_index[next_state]
                                                            edges_graph[curr_state_index].append(next_state_index)
                                                        continue

                                                    next_state = (a1, a2, r1, r2, k1, k2, q1, q2, t1, t2, (p+1)%3 )
                                                    next_state_index = map_state_to_index[next_state]
                                                    edges_graph[curr_state_index].append(next_state_index)
                                                

    n = 0
    all_transitions = {}
    players = [0, 1]
    edges_graph_with_removed_transitions = copy(edges_graph)

    player_index = 0
    vertex = 0
    value = {}
    while True:
        value = {}
        for vertex in vertices_graph:
            for player_index in players:
                if check_if_always_winning_stratergy(vertices_graph, edges_graph_with_removed_transitions, map_vertex_to_player, bad_states[player_index], vertex, player_index) == True:
                    value[player_index, vertex] = 1
                elif check_if_never_winning_stratergy(vertices_graph, edges_graph_with_removed_transitions, map_vertex_to_player, bad_states[player_index], vertex, player_index) == True:
                    value[player_index, vertex] = -1
                else:
                    value[player_index, vertex] = 0
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

    print("The set of dominated strategies: ")
    for t in all_transitions:
        print(t[1], "->", t[2])