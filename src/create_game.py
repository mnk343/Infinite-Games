from check_for_winning_strategy import *

if __name__ == "__main__":
    m, n = 3, 3
    area = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    posA = [0, 0]
    posB = [2, 2]

    finalA = [2, 2]
    finalB = [0, 0]

    total_states = (m * n) ** 2
    print(total_states)

    # position_index_to_coord = {}

    # index = 0
    # for x in range(m):
    #     for y in range(n):
    #         position_index_to_coord[index] = [x, y]
    #         index += 1
    
    # positions_count = m*n

    # graph = [ [0] * positions_count ] * positions_count


    vertices_graph = set([])
    state_index_to_posA = {}
    state_index_to_posB = {}
    state_pos_to_index = {}
    map_vertex_to_player = {}

    state_index = 0
    for Ax in range(m):
        for Ay in range(n):
            for Bx in range(m):
                for By in range(n):
                    vertices_graph.add(state_index)
                    map_vertex_to_player[state_index] = 0
                    state_index_to_posA = [Ax, Ay]
                    state_index_to_posB = [Bx, By]
                    state_pos_to_index[Ax, Ay, Bx, By] = state_index
                    state_index += 1

    
    # bad states for collision
    bad_states_collision = []
    bad_states_wall = []
    bad_states = []

    for x in range(m):
        for y in range(n):
            bad_index = state_pos_to_index[x, y, x, y]
            bad_states_collision.append(bad_index)
            bad_states.append(bad_index)

    print(bad_states_collision)
    print(vertices_graph)

    for Ax in range(m):
        for Ay in range(n):
            for Bx in range(m):
                for By in range(n):
                    if area[Ax][Ay] == 1 or area[Bx][By] == 1:
                        bad_index = state_pos_to_index[Ax, Ay, Bx, By]
                        bad_states_wall.append(bad_index)
                        bad_states.append(bad_index)

    print(bad_states_wall)

    starting_state_index = state_pos_to_index[posA[0], posA[1], posB[0], posB[1]]
    winning_state_index = state_pos_to_index[finalA[0], finalA[1], finalB[0], finalB[1]]

    print(starting_state_index)
    print(winning_state_index)


    next_x = [1, -1, 0, 0]
    next_y = [0, 0, -1, 1]

    edges_graph = {}

    for Ax in range(m):
        for Ay in range(n):
            for Bx in range(m):
                for By in range(n):
                    curr_state = state_pos_to_index[Ax, Ay, Bx, By]
                    for d in range(len(next_x)):
                        new_x = Ax + next_x[d]
                        new_y = Ay + next_y[d]
                        if (new_x, new_y, Bx, By) in state_pos_to_index:
                            next_state = state_pos_to_index[new_x, new_y, Bx, By]
                            if curr_state not in edges_graph:
                                edges_graph[curr_state] = [next_state]
                            else:
                                edges_graph[curr_state].append(next_state)
                    
                    for d in range(len(next_x)):
                        new_x = Bx + next_x[d]
                        new_y = By + next_y[d]
                        if (Ax, Ay, new_x, new_y) in state_pos_to_index:
                            next_state = state_pos_to_index[Ax, Ay, new_x, new_y]
                            if curr_state not in edges_graph:
                                edges_graph[curr_state] = [next_state]
                            else:
                                edges_graph[curr_state].append(next_state)

    c = 0
    for initial_state in range(total_states):
        print( "For state v" + str(initial_state) + ": " + str(check_if_always_winning_stratergy( vertices_graph, edges_graph, map_vertex_to_player, bad_states , initial_state, 0)))
        if check_if_always_winning_stratergy( vertices_graph, edges_graph, map_vertex_to_player, bad_states , initial_state, 0) == False:
            c += 1

    print(c)
