# Compositional Synthesis using Admissible Strategies
#
**Controller Synthesis** revolves around the design and implementation of systems working in an environment to satisfy their goals. A popular approach to solve controller synthesis is to find winning strategies in graph games for the system against the environment. Safety games are a class of graph games in which the winning objective for a player is to never visit their corresponding unsafe states. However, in several cases where no winning strategies exist, we find **admissible strategies** in which players play rationally instead of being adversarial and achieve their goals. Compositional Synthesis refers to the process of realizing a controller for the entire system by breaking it into several controllers which would represent individual components. In our work, we make an attempt to design component-based controllers using Admissible strategies in multiplayer games.

This repository contains all the documents and the entire source code for the work done during our Bachelors Thesis Project under the guidance of **Prof. Purandar Bhaduri**.

## Running the code
Requirements: You would require python3 installed on your machine to run the code.
Once the repository is cloned, follow the steps as mentioned below:
### To find admissible strategies in a custom graph
- cd src
- python3 admissible_strategies.py

Once the program starts, it will ask for the graph as input, 
We demonstrate a sample for the following graph,
![Image for example](https://github.com/mnk343/Infinite-Games/blob/master/Additional_Files_And_Resources/Example1.png?raw=true)
- We have to add the number of vertices first (here it is 5)
- Now we have to input the number of edges (here it is 8)
- Now, in next 8 lines (or your count of edges lines), we add the corresponding edge (space separated)
- Next we add the number of players in the game (here, it is 2)
- Now, we add the vertices that belong to each player  (space separated)
- Then we add the bad states for each player (space separated again)
- Once this is done, we get the dominated edges

An Example input has been shown below:
![Image for output](https://github.com/mnk343/Infinite-Games/blob/master/Additional_Files_And_Resources/Output_1.png?raw=true)

- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF

### To run the Burger King robot delivery example:
- cd src
- python3 robot_delivery.py

### To run the real time scheduler example
- cd src
- python3 real_time_scheduler.py

### To see the work on 2-D robot motion planning:
We had worked on 2-D robot motion planning where we tried finding maximally permissive strategies. We moved onto other examples because this one was getting solved by translating it into a single player graph game which is very trivial to solve. 

Still, all our different test cases that we had run and all the corresponding outputs can be seen on the following notebook link:
https://github.com/mnk343/Infinite-Games/blob/master/src/Infinite_Games.ipynb

### Future Work:
For the scheduler example, we may make use of parallel programming to improve the efficiency and the run time of the program. We may generate multiple threads to make use of all the cores in the system. This would help us to get the results faster.
We could apply the algorithms and the work to other real life applications as well. We could think of more such examples.
Moreover, in all the examples we have worked on this paper, we have assumed safety objectives for all the players which may not always be the case. There are various other games/objectives that the player may want to meet such as the Bu ̈chi or the Muller games.
As a future work, we may expand our controller synthesis to include other types of objectives as well.
Even though admissible strategies was an appropriate way to allow each player meet its own objectives, we may also explore some use some other strategy for the same.



