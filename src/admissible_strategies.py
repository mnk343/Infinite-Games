from copy import copy
from check_for_winning_strategy import *

if __name__ == "__main__":
    area = [
        [0,0,0],
        [0,1,0],
        [0,0,0],
    ]
    for i in area:
        for j in i:
            print(j, end= " ")
        print()
        
    m = len(area)
    n = len(area[0])
    while(1):
        starting_x_coord_robot_1 = int(input("Enter Starting X-Coordinate for Robot 1: "))
        if starting_x_coord_robot_1 == -1:
            break
        starting_y_coord_robot_1 = int(input("Enter Starting Y-Coordinate for Robot 1: "))
        
        starting_x_coord_robot_2 = int(input("Enter Starting X-Coordinate for Robot 2: "))
        starting_y_coord_robot_2 = int(input("Enter Starting Y-Coordinate for Robot 2: "))
        
        posA = [starting_x_coord_robot_1, starting_y_coord_robot_1]
        posB = [starting_x_coord_robot_2, starting_y_coord_robot_2]

        final_x_coord_robot_1 = int(input("Enter Final X-Coordinate for Robot 1: "))
        final_y_coord_robot_1 = int(input("Enter Final Y-Coordinate for Robot 1: "))
        
        final_x_coord_robot_2 = int(input("Enter Final X-Coordinate for Robot 2: "))
        final_y_coord_robot_2 = int(input("Enter Final Y-Coordinate for Robot 2: "))
        
        finalA = [final_x_coord_robot_1, final_y_coord_robot_1]
        finalB = [final_x_coord_robot_2, final_y_coord_robot_2]

        time_bound = int(input("Enter Time Bound: "))
        number_of_players = 2

        total_states = (m * n) ** 2 * time_bound * number_of_players
        print(total_states)
        vertices_graph = set([])
        state_pos_to_index = {}
        state_index_to_pos = {}
        map_vertex_to_player = {}

        state_index = 0
        for Ax in range(m):
            for Ay in range(n):
                for Bx in range(m):
                    for By in range(n):
                        for time in range(time_bound+1):
                            for player in range(number_of_players):
                                vertices_graph.add(state_index)
                                map_vertex_to_player[state_index] = 0
                                state_pos_to_index[Ax, Ay, Bx, By, time, player] = state_index
                                state_index_to_pos[state_index] = [Ax, Ay, Bx, By, time, player]
                                state_index += 1
        auxiliary_good_state = (len(area),len(area[0]),len(area),len(area[0]),-1,-1)
        auxiliary_bad_state = (-1,-1,-1,-1,0,-1)

        # Auxiliary bad state
        state_pos_to_index[auxiliary_bad_state] = state_index
        state_index_to_pos[state_index] = auxiliary_bad_state
        map_vertex_to_player[state_index] = 0
        state_index += 1

        # Auxiliary good state
        state_pos_to_index[auxiliary_good_state] = state_index
        state_index_to_pos[state_index] = auxiliary_good_state
        map_vertex_to_player[state_index] = 0
        state_index += 1

        vertices_graph.add(state_pos_to_index[auxiliary_good_state])
        vertices_graph.add(state_pos_to_index[auxiliary_bad_state])

        # bad states for collision
        bad_states_all = set([])

        for x in range(m):
            for y in range(n):
                for time in range(time_bound+1):
                    for player in range(number_of_players):
                        bad_index = state_pos_to_index[x, y, x, y, time, player]
                        bad_states_all.add(bad_index)

        # print(bad_states_collision)
        # print(vertices_graph)

        for Ax in range(m):
            for Ay in range(n):
                for Bx in range(m):
                    for By in range(n):
                        if area[Ax][Ay] == 1 or area[Bx][By] == 1:
                            for time in range(time_bound+1):
                                for player in range(number_of_players):
                                    bad_index = state_pos_to_index[Ax, Ay, Bx, By, time, player]
                                    bad_states_all.add(bad_index)

        # print(bad_states_wall)

        starting_state_index = state_pos_to_index[posA[0], posA[1], posB[0], posB[1], 0, 1]
        winning_state_index = state_pos_to_index[auxiliary_good_state]

        # print(starting_state_index)
        # print(winning_state_index)

        next_x = [1, -1, 0, 0]
        next_y = [0, 0, -1, 1]

        edges_graph = {}

        for Ax in range(m):
            for Ay in range(n):
                for Bx in range(m):
                    for By in range(n):
                        for time in range(time_bound):
                            for player in range(number_of_players):
                                curr_state = state_pos_to_index[Ax, Ay, Bx, By, time, player]
                                if Ax == finalA[0] and Ay == finalA[1] and Bx == finalB[0] and By == finalB[1]:
                                    continue
                                if curr_state not in edges_graph:
                                    edges_graph[curr_state] = [curr_state]
                                else:
                                    edges_graph[curr_state].append(curr_state)
                                if player == 0:
                                    if curr_state not in edges_graph:
                                        edges_graph[curr_state] = [state_pos_to_index[Ax, Ay, Bx, By, time, (player+1)%2]]
                                    else:
                                        edges_graph[curr_state].append(state_pos_to_index[Ax, Ay, Bx, By, time, (player+1)%2])
                                    for d in range(len(next_x)):
                                        new_x = Ax + next_x[d]
                                        new_y = Ay + next_y[d]
                                        if (new_x, new_y, Bx, By, time, (player+1)%2) in state_pos_to_index:
                                            next_state = state_pos_to_index[new_x, new_y, Bx, By, time, (player+1)%2]
                                            if curr_state not in edges_graph:
                                                edges_graph[curr_state] = [next_state]
                                            else:
                                                edges_graph[curr_state].append(next_state)
                                else:    
                                    if curr_state not in edges_graph:
                                        edges_graph[curr_state] = [state_pos_to_index[Ax, Ay, Bx, By, time+1, (player+1)%2]]
                                    else:
                                        edges_graph[curr_state].append(state_pos_to_index[Ax, Ay, Bx, By, time+1, (player+1)%2])
                                    for d in range(len(next_x)):
                                        new_x = Bx + next_x[d]
                                        new_y = By + next_y[d]
                                        if (Ax, Ay, new_x, new_y, (time+1), (player+1)%2 ) in state_pos_to_index:
                                            next_state = state_pos_to_index[Ax, Ay, new_x, new_y, (time+1), (player+1)%2]
                                            if curr_state not in edges_graph:
                                                edges_graph[curr_state] = [next_state]
                                            else:
                                                edges_graph[curr_state].append(next_state)

        for time in range(time_bound+1):
            for player in range(number_of_players):
                good_temp_state = (finalA[0],finalA[1],finalB[0],finalB[1], time ,player)
                good_temp_state_index = state_pos_to_index[good_temp_state]
                if good_temp_state_index not in edges_graph:
                    edges_graph[good_temp_state_index] = [state_pos_to_index[auxiliary_good_state]]
                else:
                    edges_graph[good_temp_state_index].append(state_pos_to_index[auxiliary_good_state])
                # edges_graph[good_temp_state_index].append(state_pos_to_index[auxiliary_good_state])
                # print(good_temp_state_index)
        # print(state_index)
        # exit(1)
        for Ax in range(m):
            for Ay in range(n):
                for Bx in range(m):
                    for By in range(n):
                        for player in range(number_of_players):
                            if Ax == finalA[0] and Ay == finalA[1] and Bx == finalB[0] and By == finalB[1]:
                                continue
                            if state_pos_to_index[Ax, Ay, Bx, By, time_bound, player] not in edges_graph:
                                edges_graph[state_pos_to_index[Ax, Ay, Bx, By, time_bound, player]] = [state_pos_to_index[auxiliary_bad_state]]
                            else:
                                edges_graph[state_pos_to_index[Ax, Ay, Bx, By, time_bound, player]].append(state_pos_to_index[auxiliary_bad_state])
        edges_graph[state_pos_to_index[auxiliary_good_state]] = [state_pos_to_index[auxiliary_good_state]]
        edges_graph[state_pos_to_index[auxiliary_bad_state]] = [state_pos_to_index[auxiliary_bad_state]]
    # vertices_graph = {0,1,2,3,4}
    # edges_graph = {
    #                 0: [1],
    #                 1: [2,3],
    #                 2: [0,4],
    #                 3: [4],
    #                 4: [3,4]
    # }

    # map_vertex_to_player = { 0:0 , 1:1, 2:0 , 3:0, 4:1}

        bad_states = [
            bad_states_all,
            {}
        ]


        # vertices_graph = {0,1,2,3,4}
        # edges_graph = {
        #                 0: [1,4],
        #                 1: [0,2],
        #                 2: [1,3],
        #                 3: [3],
        #                 4: [2,4]
        # }

        # map_vertex_to_player = { 0:0 , 1:1, 2:0 , 3:1, 4:1}

        # bad_states = [
        #     {2},
        #     {3}
        # ]
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
        edges_graph_dominated = {}
        for t in all_transitions:
            print(t[1], "->", t[2])
            print(state_index_to_pos[t[1]])
            print(state_index_to_pos[t[2]])
            print()
            if t[1] not in edges_graph_dominated:
                edges_graph_dominated[t[1]] = [t[2]]
            else:
                edges_graph_dominated[t[1]].append(t[2])

        current_state = state_pos_to_index[posA[0],posA[1],posB[0],posB[1],0,0]
        # while(1):
        #     for possible_state in edges_graph[current_state]:
        #         tempA = state_index_to_pos[current_state]
        #         tempB = state_index_to_pos[possible_state]
        #         if (tempB[0] == finalA[0] and tempB[1] == finalA[1]) or (tempB[2] == finalB[0] and tempB[3] == finalB[1]) or not( tempA[0] == tempB[0] and tempA[1] == tempB[1] and tempA[2] == tempB[2] and tempA[3] == tempB[3] ):
        #             if ((current_state not in edges_graph_dominated) or (current_state in edges_graph_dominated and possible_state not in edges_graph_dominated[current_state] )):
        #                 print( str(current_state) + " -> " + str(possible_state) )
        #                 print(state_index_to_pos[current_state])
        #                 print(state_index_to_pos[possible_state])
        #                 print()
        #                 current_state = possible_state
        #                 break
        #     if current_state == state_pos_to_index[auxiliary_good_state] or current_state == state_pos_to_index[auxiliary_bad_state]:
        #         break
        exit(0)
