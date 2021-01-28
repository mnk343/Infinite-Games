if __name__ == "__main__":
    area = [
        [1, 2, 1, 0, 0, 2],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 1],
        [0, 0, 0, 2, 1, 0],
        [1, 0, 1, 0, 0, 0],
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

        vertices_graph = set([])
        state_pos_to_index = {}
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
                                state_index += 1
        # print(state_pos_to_index[0,0,0,0,10,0])
        # exit(0)
        auxiliary_good_state = (len(area),len(area[0]),len(area),len(area[0]),-1,-1)
        auxiliary_bad_state = (-1,-1,-1,-1,0,-1)

        # Auxiliary bad state
        state_pos_to_index[auxiliary_bad_state] = state_index
        state_index += 1

        # Auxiliary good state
        state_pos_to_index[auxiliary_good_state] = state_index
        state_index += 1

        # bad states for collision
        bad_states_collision = []
        bad_states_wall = []
        bad_states = []

        for x in range(m):
            for y in range(n):
                for time in range(time_bound+1):
                    for player in range(number_of_players):
                        bad_index = state_pos_to_index[x, y, x, y, time, player]
                        bad_states_collision.append(bad_index)
                        bad_states.append(bad_index)

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
                                    bad_states_wall.append(bad_index)
                                    bad_states.append(bad_index)

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
                                    for d in range(len(next_x)):
                                        new_x = Ax + next_x[d]
                                        new_y = Ay + next_y[d]
                                        if (new_x, new_y, Bx, By, time, (player+1)%2) in state_pos_to_index:
                                            next_state = state_pos_to_index[new_x, new_y, Bx, By, time+1, (player+1)%2]
                                            if curr_state not in edges_graph:
                                                edges_graph[curr_state] = [next_state]
                                            else:
                                                edges_graph[curr_state].append(next_state)
                                else:    
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
                            
        # for initial_state in range(total_states):
        initial_state = state_pos_to_index[ posA[0], posA[1], posB[0], posB[1], 0, 0]
        bad_states.append(state_pos_to_index[auxiliary_bad_state])
        print( "For given state v: " + str(check_if_always_winning_stratergy( vertices_graph, edges_graph, map_vertex_to_player, bad_states , initial_state, 0)))
