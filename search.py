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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    path = util.Stack()												#Using stack as the queuing function.
    visited = []
    visited.append(problem.getStartState())							#Pushing the start node.
    dictionary = {}													#For storing the parent.
    if problem.isGoalState(problem.getStartState()):				# if goal state is reached.
    	return []
    first_level = problem.getSuccessors(problem.getStartState())		#Getting Successor
    for items in first_level:
    	path.push(items)
    	dictionary[items] = problem.getStartState()
    	#visited.append(items)
    while (path.isEmpty() == False):
    	nextNode = path.pop()
    	if nextNode[0] not in visited:
    		visited.append(nextNode[0])
    		if problem.isGoalState(nextNode[0]):
    			return findPath(dictionary,nextNode,problem.getStartState())
    		for successors in problem.getSuccessors(nextNode[0]):
    			if successors[0] in visited:
    				continue
    			else:
    				dictionary[successors] = nextNode
    				path.push(successors)
    				
    return []
	
def findPath(dictionary,goal,start):
	   current = goal
	   #print dictionary[((5, 6, 1, 1, 1, 6, 6, 6), 'West', 1)]
	   #print dictionary[((6, 6, 1, 1, 1, 6, 6, 6), 'East', 1)]
	   solution = []
	   while(current != start):
	   	#print "Current is : ",current[1],dictionary[current]
	   	solution.insert(0,current[1])
	   	current = dictionary[current]
	   return solution
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    path = util.Queue()
    visited = []
    visited.append(problem.getStartState())
    dictionary = {}
    if problem.isGoalState(problem.getStartState()):
    	return []
    first_level = problem.getSuccessors(problem.getStartState())
    for items in first_level:
    	path.push(items)
    	dictionary[items] = problem.getStartState()
    	#visited.append(items)
    while (path.isEmpty() == False):
    	nextNode = path.pop()
    	#print "state : ",nextNode[0]
    	if nextNode[0] not in visited:
    		visited.append(nextNode[0])
    		if problem.isGoalState(nextNode[0]):
    			return findPath(dictionary,nextNode,problem.getStartState())
    		for successors in problem.getSuccessors(nextNode[0]):
    			if successors[0] in visited:
    				continue
    			else:
    				dictionary[successors] = nextNode
    				path.push(successors)
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    path = util.PriorityQueue()
    visited = []
    visited.append(problem.getStartState())
    dictionary = {}
    if problem.isGoalState(problem.getStartState()):
    	return []
    first_level = problem.getSuccessors(problem.getStartState())
    for items in first_level:
    	#print items
    	path.push(items,items[2])
    	dictionary[items] = problem.getStartState()
    	#visited.append(items)
    while (path.isEmpty() == False):
    	nextNode = path.pop()
    	if nextNode[0] not in visited:
    		visited.append(nextNode[0])
    		if problem.isGoalState(nextNode[0]):
    			return findPath(dictionary,nextNode,problem.getStartState())
    		for successors in problem.getSuccessors(nextNode[0]):
    			if successors[0] in visited:
    				continue
    			else:
    				dictionary[successors] = nextNode
    				cost = findCost(dictionary,successors,problem.getStartState())
    				path.push(successors,cost)
    return []

def findCost(dictionary,goal,start):
	   current = goal
	   solution = []
	   cost = 0
	   while(current != start):
	   	cost = cost + current[2]
	   	current = dictionary[current]
	   return cost
	   
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    path = util.PriorityQueue()
    visited = []
    dictionary = {}
    visited.append(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
    	return []
    first_level = problem.getSuccessors(problem.getStartState())
    for items in first_level:
    	#print items
    	path.push(items,items[2] + heuristic(items[0],problem))
    	dictionary[items] = problem.getStartState()
    	#visited.append(items)
    while (path.isEmpty() == False):
    	nextNode = path.pop()
    	if nextNode[0] not in visited:
    		visited.append(nextNode[0])
    		if problem.isGoalState(nextNode[0]):
    			return findPath(dictionary,nextNode,problem.getStartState())
    		for successors in problem.getSuccessors(nextNode[0]):
    			if successors[0] in visited:
    				continue
    			else:
    				dictionary[successors] = nextNode
    				cost = findCost(dictionary,successors,problem.getStartState())
    				#print heuristic(successors[0],problem)
    				#print successors[0]
    				path.push(successors,cost+heuristic(successors[0],problem))
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
