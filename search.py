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
    return [s, s, w, s, w, w, s, w]


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
    visited=[]
    point = problem.getStartState()
    condition = True
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    
    first_stack = util.Stack()
    visited_stack = []
    first_stack.push((problem.getStartState(),[]))
    if problem.isGoalState(problem.getStartState):
        return []
    while not first_stack.isEmpty():
        current_node,path = first_stack.pop()
        if current_node not in visited_stack:
            visited_stack.append(current_node)

            if problem.isGoalState(current_node):
                return path
            
            for neighbors in problem.getSuccessors(current_node):
                newPath = path+ [neighbors[1]]
                first_stack.push((neighbors[0],newPath))
        

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    queue.push((problem.getStartState(),'',0))
    visited = set()
    while not queue.isEmpty():
        curr = queue.pop()
        curr_point = curr[0]
        path = curr[1] 
        if problem.isGoalState(curr_point):
            #print(path,'aispodiaposd')
            return path
        if curr_point not in visited:
            for neighbour in problem.getSuccessors(curr_point):
                    #print(path)
                    latest_path = list(path)
                    #print(latest_path)
                    latest_path.append(neighbour[1][0::])
                    #print(latest_path)
                    queue.push((neighbour[0],latest_path,1))
            visited.add(curr_point)
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # queue = util.PriorityQueue()
    # queue.push((problem.getStartState(),'',0),0)
    # visited = set()
    # if problem.isGoalState(problem.getStartState()):
    #     path = queue.pop()
    #     return path[1]
    # while not queue.isEmpty():
    #     curr = queue.pop()
    #     #print(curr)
    #     curr_point = curr[0]
    #     path = curr[1] 
    #     path_cost = curr[2]
    #     visited.add(curr_point)
    #     if problem.isGoalState(curr_point):
    #         return path     
    #     for neighbour in problem.getSuccessors(curr_point):
    #             latest_path = list(path)
    #             latest_path.append(neighbour[1][0::])
    #             neighbour_cost = path_cost+neighbour[2]
    #             new_element = (neighbour[0],latest_path,neighbour_cost)
    #             if new_element in queue.heap:
    #                 queue.update(new_element,neighbour_cost)
    #             elif neighbour[0] not in visited and new_element not in queue.heap: 
    #                 queue.push(new_element,neighbour_cost)
    queue = util.PriorityQueue()
    queue.push((problem.getStartState(),'',0),0)
    visited = set()
    while not queue.isEmpty():
        curr = queue.pop()
        curr_point = curr[0]
        path = curr[1] 
        curr_cost = curr[2]
        if problem.isGoalState(curr_point):
            #print(path,'aispodiaposd')
            return path
        if curr_point not in visited:
            for neighbour in problem.getSuccessors(curr_point):
                    #print(path)
                    latest_path = list(path)
                    #print(latest_path)
                    latest_path.append(neighbour[1][0::])
                    #print(latest_path)
                    cost = neighbour[2]+curr_cost
                    queue.push((neighbour[0],latest_path,cost),cost)
            visited.add(curr_point)
        


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    queue.push((problem.getStartState(),'',0),0)
    visited = set()
    while not queue.isEmpty():
        curr = queue.pop()
        curr_point = curr[0]
        path = curr[1] 
        curr_cost = curr[2]
        if problem.isGoalState(curr_point):
            #print(path,'aispodiaposd')
            return path
        if curr_point not in visited:
            for neighbour in problem.getSuccessors(curr_point):
                    #print(path)
                    latest_path = list(path)
                    #print(latest_path)
                    latest_path.append(neighbour[1][0::])
                    #print(latest_path)
                    cost = neighbour[2]+curr_cost
                    priority = cost + heuristic(neighbour[0],problem)
                    queue.push((neighbour[0],latest_path,cost),priority)
            visited.add(curr_point)
            



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
