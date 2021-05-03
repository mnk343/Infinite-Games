from copy import copy
from check_for_winning_strategy import *

if __name__ == "__main__":

    # vertices_graph = {0,1,2,3,4}
    # edges_graph = {
    #                 0: [1,4],
    #                 1: [0,2],
    #                 2: [1,3],
    #                 3: [3],
    #                 4: [2]
    # }

    # map_vertex_to_player = { 0:0 , 1:1, 2:0 , 3:1, 4:1}

    # bad_states = [
    #     {2},
    #     {3}
    # ]

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


    vertices_graph = set({})
    edges_graph = {}
    map_vertex_to_player = {}
    bad_states = []
    players = []


    num_of_vertices = int(input("Enter number of vertices: "))
    for v in range(0, num_of_vertices):
    	vertices_graph.add(v)

    print("Now, we will construct the edges graph...")

    num_of_edges = int(input("Enter number of egdes: "))
    print("In next " + str(num_of_edges) + " lines, enter space separated vertices having edge between them:")
    for edge in range(num_of_edges):
    	a, b = [int(x) for x in input().split()]
    	if a not in edges_graph: 
    		edges_graph[a] = []
    	edges_graph[a].append(b)

    num_of_players = int(input("Enter number of players: "))
    for p in range(num_of_players):
    	players.append(p)


    print("Now, enter all the vertices (space-separated) owned by each player:")

    for p in players:
    	p_vertices = [int(x) for x in input("Player "+ str(p) + ": ").split()]
    	for v in p_vertices:
    		map_vertex_to_player[v] = p


    print("Now, enter all the bad vertices (space-separated) for each player:")

    for p in players:
    	p_vertices = set({int(x) for x in input("Player "+ str(p) + ": ").split()})
    	bad_states.append(p_vertices)


    # print(vertices_graph)
    # print(edges_graph)
    # print(players)
    # print(map_vertex_to_player)
    # print(bad_states)
    print("Finding admissible strategies: ")

    all_transitions = {}
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