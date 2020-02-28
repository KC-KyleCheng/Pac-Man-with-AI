# Pac-Man-with-AI

Applied AI on Pac-Man using Python such that the Pac-Man can find the shortest path to the desired destinations and navigate by itself.
Utilized Breadth-first search, Depth-first search, and A* search algorithms to help Pac-Man identify the shortest path.

Use the following commands to execute the program:

Depth-First Search:

python pacman.py -l tinyMaze -p SearchAgent

python pacman.py -l mediumMaze -p SearchAgent

python pacman.py -l bigMaze -z .5 -p SearchAgent

python pacman.py -l openMaze -z .5 -p SearchAgent

Breadth-First Search :

python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs

python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

python pacman.py -l bigMaze -p SearchAgent -a fn=bfs

python pacman.py -l openMaze -p SearchAgent -a fn=bfs

A* Search:

python pacman.py -l tinyMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic


Impletmented by me:

"search.py":

	def depthFirstSearch(problem)

	def breadthFirstSearch(problem)

	def aStarSearch(problem, heuristic=nullHeuristic)

"searchAgents.py":

class CornersProblem(search.SearchProblem):

	def getStartState(self)

	def isGoalState(self, state)

	def getSuccessors(self, state)

	
	def cornersHeuristic(state, problem)
