import time

graph = {}
state_s = ["idle" , "writing" , "done"]
state_t = [1, 2, 3, 4]

good = 5
bad = 0

# states = []

# for s in state_s:
# 	for t in state_t:
# 		states.append((s, t))

# print(states)

# state, action, env

for t in range(1, 5):
	graph[ ("idle", t), ("wait", "idle") ] = ("idle", t-1)
	graph[ ("idle", t), ("wait", 'b') ] = ("idle", t-1)

	graph[ ("idle", t), ("wr", "idle") ] = ("writing", t-1)
	graph[ ("idle", t), ("wr", "busy") ] = ("writing", t-1)

	if t >= 2:
		graph[ ("writing", t), ("wr", "idle") ] = ("done", good)
		graph[ ("writing", t), ("wr", "busy") ] = ("writing", t-1)
	else:
		graph[ ("writing", t), ("wr", "idle") ] = ("", bad)
		graph[ ("writing", t), ("wr", "busy") ] = ("", bad)


system_halt = False

current_states = [("idle", 4), ("idle", 4)]
environment = "idle"
output = ["idle", "idle"]

writing_time = [4, 4]
time_so_far = 0
running_systems = 2
system_running = [0, 0]

def move(player):

	global running_systems

	if( current_states[player][1] == bad or current_states[player][1] == good ):
		return "idle"

	if( time_so_far >= writing_time[player] ):
		current_states[player] = graph [ current_states[player] , ("wr" , environment) ]
	else:
		return "idle"
		curr_time = current_states[player]
		current_states[player] = graph [ current_states[player] , ("wait" , environment) ]

	if current_states[player][1] == bad:
		running_systems -= 1

	if current_states[player][1] == good:
		running_systems -= 1
		print("Packet for player " + str(player) + " sent!" )


	if current_states[player] == "writing":
		return "busy"

	return "idle"

while not system_halt:
	# move of player 1
	output[0] = move(0)
	environment = output[0]

	output[1] = move(1)
	environment = output[1]

	time.sleep(1)
	print("Time elapsed: " + str(time_so_far))
	time_so_far += 1

	if running_systems == 0:
		system_halt = True		

