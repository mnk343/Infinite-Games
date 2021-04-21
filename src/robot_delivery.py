from copy import copy
from check_for_winning_strategy import *

if __name__ == "__main__":

    vertices_graph = {1,2,3,4,5,6,7,8,9,10}
    edges_graph = {
                    1: [2,3],
                    2: [4,7],
                    3: [1,6],
                    4: [3,8],
                    5: [4,7],
                    6: [5,9],
                    7: [8,9],
                    8: [7,10],
                    9: [7,10],
                    10: [8,9]
    }

    map_vertex_to_player = {    1: 0, 
                                2: 1,
                                3: 1,
                                4: 0,
                                5: 1,
                                6: 0,
                                7: 0,
                                8: 1,
                                9: 1,
                                10: 0
    }

    bad_states = [
        {7,8,9,10},
        {7,8,9,10},
    ]

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