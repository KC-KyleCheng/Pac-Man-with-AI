# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import util

class SearchProblem:

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    print ( problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )

    """
 
    from util import Stack
    candidates = Stack()
    candidates.push([problem.getStartState(), [], 0])
    visited = []
    while True:

        if candidates.isEmpty():
            print ("ERROR: stack is empty!")
            return []
        node, path, cost = candidates.pop()

        if node in visited: 
            continue
        visited.append(node)        

        if problem.isGoalState(node):
            return path
        else:            
            for state, move, distance in problem.getSuccessors(node):
                candidates.push([state, path+[move], cost+distance])
               

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """

    from util import Queue
    candidates = Queue()
    candidates.push([problem.getStartState(), [], 0])
    visited = []
    while True:
        if candidates.isEmpty():
            print ("ERROR: queue is empty!")
            return []
        node, path, cost = candidates.pop()

        if node in visited: 
            continue
        visited.append(node)        

        if problem.isGoalState(node):
            return path
        else:            
            for state, move, distance in problem.getSuccessors(node):
                if state not in visited:
                    candidates.push([state, path+[move], cost+distance])



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    

    from util import Queue
    candidates = []
    candidates.append([problem.getStartState(), [], 0, heuristic(problem.getStartState(), problem)])
    visited = []
    while True:

        if len(candidates) == 0:
            print ("ERROR: candidates list is empty!")
            return []

        lowest = candidates[0][2] + candidates[0][3]
        lowest_index = 0
        for i in range(len(candidates)):
            if (candidates[i][2] + candidates[i][3]) < lowest:
                lowest = candidates[i][2] + candidates[i][3]
                lowest_index = i
        
        node, path, cost, manhattan = candidates.pop(lowest_index)

        if node in visited: 
            continue
        visited.append(node)        

        if problem.isGoalState(node):
            return path
        else:            
            for state, move, distance in problem.getSuccessors(node):
                candidates.append([state, path+[move], cost+distance, heuristic(state, problem)])


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
