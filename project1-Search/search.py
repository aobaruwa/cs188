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
from platform import node
from random import choice
from time import sleep
from _elementtree import Element


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
    
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    frontier = util.Stack()
    explored = set({})
    solution = []
    result = []

    mine = []
    parent_dict = {}
    counter = 0
    
    #traceable_end.append(problem.getStartState())
    frontier.push(problem.getStartState())
    while not frontier.isEmpty():
        choice_node = frontier.pop()
        
        if len(choice_node) > 1:# store all tracks starting from node2 (node2 accounts for the start node)
            nxt = choice_node[0]
            solution.append(choice_node)
        
        else: nxt = choice_node # the start state 
        
        if problem.isGoalState(nxt): # Bingo, found goal State!
            # return the right path
            solution.reverse()
            #print "good =", solution #check
            # copy the solution into mine
            mine = solution
            i = 0
            #print "parent dict =", parent_dict # check
            while True:
                #print i
                if parent_dict[solution[i]] == problem.getStartState():
                    
                    break
                if parent_dict[solution[i]] != solution[i + 1][0]:
                    solution.remove(solution[i + 1])
                    #print "sol-",solution #check
                    continue
                
                i += 1    
                    #mine.reverse()
                    #print "mine -", mine
                    #print "parent_dict =", parent_dict
            
            #print "mine =", mine
            for e in mine:
                a = e[1]
                if parent_dict[e] == problem.getStartState():
                    
                    #print a, type(a)
                    result.append(a)
                    result.reverse()
                    #print result
                    break
                result.append(a)
                #print result
                
            #print "answer =", solution.reverse()
            return result
                #mine.append(e[1])
            
            break
        
        # expand the next node(its state in particular) if not the goal node
        if counter > 0:
            #(nxt, action, cost) = choice_node
            choice_node = choice_node[0]  
        explored.add(choice_node)
        successors = problem.getSuccessors(choice_node)
        

        for elem in successors:
            #nxt, action, cost = elem
            if elem[0] not in explored:
                frontier.push(elem)
            #attach each child node to its parent
            parent_dict[elem] = choice_node
         
        counter += 1       
                
    return None        
        


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    frontier = util.Queue()
    explored = set({})
    solution = []
    result = []

    mine = []
    parent_dict = {}
    counter = 0
    
    #traceable_end.append(problem.getStartState())
    frontier.push(problem.getStartState())
    while not frontier.isEmpty():
        choice_node = frontier.pop()
        
        
        if counter > 0:# store all tracks starting from node2 (node2 accounts for the start node)
            nxt = choice_node[0]
            if choice_node not in solution: solution.append(choice_node)
        
        else: 
            nxt = choice_node # the start state 
            explored.add(nxt)
            
        if problem.isGoalState(nxt): # Bingo, found goal State!
            # return the right path
            solution.reverse()
            #print "good =", solution #check
            #print len(solution)
            # copy the solution into mine
            mine = solution
            i = 0
            #print "parent dict =", parent_dict # check
            while True:
                #print i
                if parent_dict[solution[i]] == problem.getStartState():
                    
                    break
                if parent_dict[solution[i]] != solution[i + 1][0]:
                    solution.remove(solution[i + 1])
                    #print "sol-",solution #check
                    continue
                
                i += 1    
                    #mine.reverse()
                    #print "mine -", mine
                    #print "parent_dict =", parent_dict
            
            #print "mine =", mine
            for e in mine:
                a = e[1]
                if parent_dict[e] == problem.getStartState():
                    
                    #print a, type(a)
                    result.append(a)
                    result.reverse()
                    #print result
                    break
                result.append(a)
                #print result
                
            #print "answer =", solution.reverse()
            #print "parent_dict -", parent_dict
            #print "explored-", explored
            return result
                #mine.append(e[1])
            
            break
        
        # expand the next node(its state in particular) if not the goal node
        if counter > 0:
            #(nxt, action, cost) = choice_node
            choice_node = choice_node[0]
            successors = problem.getSuccessors(choice_node)
        #if choice_node not in explored and counter > 0: 
        #explored.add(choice_node[0])
        else: 
            successors = problem.getSuccessors(choice_node)
        #elif choice_node not in explored and counter == 0:
        #explored.add(choice_node)
        #successors = problem.getSuccessors(choice_node)

        for elem in successors:

            #nxt, action, cost = elem
            if elem[0] not in explored:
                frontier.push(elem)
                explored.add(elem[0])
                #attach each child node to its parent
                parent_dict[elem] = choice_node
            #explored.add(elem)
        counter += 1       
                
    return None 


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    frontier = util.PriorityQueue()
    explored = set({})
    solution = []
    result = []

    mine = []
    parent_dict = {}
    counter = 0
    costSoFar = {}
    goal_states = []
    
    #traceable_end.append(problem.getStartState())
    frontier.push(problem.getStartState(), 0)
    while not frontier.isEmpty():
        choice_node = frontier.pop()
        #print "choice_node-", choice_node
        if counter > 0:
            costSoFar[choice_node[0]] = costSoFar[parent_dict[choice_node]] + choice_node[2]
            
            #print "costSofar-", costSoFar
        else: costSoFar[choice_node] = 0
        
        if len(choice_node) > 1:# store all tracks starting from node2 (node2 accounts for the start node)
            nxt = choice_node[0]
            if choice_node not in solution: solution.append(choice_node)
        
        else: 
            nxt = choice_node # the start state 
            explored.add(nxt)
            
        if counter > 0:
            
            if problem.isGoalState(nxt): # Bingo, found goal State!
                #print "goal_states-", goal_states
                costs = []
                for e in goal_states:
                    costs.append(e[2])
                minimum = min(costs)
                #print "minCost-", minimum
                for e in goal_states:
                    if e[2] != minimum and e in solution:
                        solution.remove(e)
                    elif e[2] == minimum and e not in solution:
                        solution.append(e)
                # return the right path
                solution.reverse()
                #print "good =", solution #check
                #print len(solution)
                # copy the solution into mine
                mine = solution
                i = 0
                #print "parent dict =", parent_dict # check
                while True:
                    #print i
                    if parent_dict[solution[i]] == problem.getStartState():
                        
                        break
                    if parent_dict[solution[i]] != solution[i + 1][0]:
                        solution.remove(solution[i + 1])
                        #print "sol-",solution #check
                        continue
                    
                    i += 1    
                        #mine.reverse()
                        #print "mine -", mine
                        #print "parent_dict =", parent_dict
                
                #print "mine =", mine
                for e in mine:
                    a = e[1]
                    if parent_dict[e] == problem.getStartState():
                        
                        #print a, type(a)
                        result.append(a)
                        result.reverse()
                        #print "result-", result
                        break
                    result.append(a)
                    #print result
                    
                #print "answer =", solution.reverse()
                #print "parent_dict -", parent_dict
                #print "explored-", explored
                #print "result-", result
                return result
                    #mine.append(e[1])
                
                break
        
        # expand the next node(its state in particular) if not the goal node
        if counter > 0:
            #(nxt, action, cost) = choice_node
            choice_node = choice_node[0]
            successors = problem.getSuccessors(choice_node)
        #if choice_node not in explored and counter > 0: 
        #explored.add(choice_node[0])
        else: 
            successors = problem.getSuccessors(choice_node)
        #elif choice_node not in explored and counter == 0:
        #explored.add(choice_node)
        #successors = problem.getSuccessors(choice_node)
        for elem in successors:
            if problem.isGoalState(elem[0]):
                goal_states.append(elem)
                parent_dict[elem] = choice_node
        
        for elem in successors:

            #nxt, action, cost = elem
            if elem[0] not in explored:
                frontier.push(elem, (elem[2]) + costSoFar[choice_node])
                explored.add(elem[0])
                #attach each child node to its parent
                parent_dict[elem] = choice_node
                
                
            #explored.add(elem)
        counter += 1       
        #frontier.get_frontier()
        #sleep(0.1)
    return None 


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    frontier = util.PriorityQueue()
    explored = set({})
    solution = []
    result = []

    mine = []
    parent_dict = {}
    counter = 0
    costSoFar = {}
    goal_states = []
    
    #traceable_end.append(problem.getStartState())
    frontier.update(problem.getStartState(), 0)
    while not frontier.isEmpty():
        #if counter == 0:
        #    choice_node = frontier.pop()
        #elif counter > 0 and choice_node not in explored:
        choice_node = frontier.pop()
            
        
        #print "choice_node-", choice_node
        if counter > 0 and choice_node[0] not in explored:
            costSoFar[choice_node[0]] = costSoFar[parent_dict[choice_node]] + choice_node[2] 
            nxt = choice_node[0]
            if choice_node not in solution: solution.append(choice_node)
            #print "heuristic value-", heuristic(choice_node[0], problem)
            #print "costSofar-", costSoFar
                
        #if len(choice_node) > 1:# store all tracks starting from node2 (node2 accounts for the start node)
        elif counter == 0: 
            costSoFar[choice_node] = 0
            nxt = choice_node # the start state 
        
        

            
        if problem.isGoalState(nxt): # Bingo, found goal State!
            #print "goal_states-", goal_states
            costs = []
            for e in goal_states:
                costs.append(e[2])
            minimum = min(costs)
            #print "minCost-", minimum
            for e in goal_states:
                if e[2] != minimum and e in solution:
                    solution.remove(e)
                elif e[2] == minimum and e not in solution:
                    solution.append(e)
            # return the right path
            solution.reverse()
            print "good =", solution #check
            #print len(solution)
            # copy the solution into mine
            mine = solution
            i = 0
            #print "parent dict =", parent_dict # check
            while True:
                #print i
                if parent_dict[solution[i]] == problem.getStartState():
                    
                    break
                if parent_dict[solution[i]] != solution[i + 1][0]:
                    solution.remove(solution[i + 1])
                    #print "sol-",solution #check
                    continue
                
                i += 1    
                    #mine.reverse()
                    #print "mine -", mine
                    #print "parent_dict =", parent_dict
            
            #print "mine =", mine
            for e in mine:
                a = e[1]
                if parent_dict[e] == problem.getStartState():
                    
                    #print a, type(a)
                    result.append(a)
                    result.reverse()
                    #print "result-", result
                    break
                result.append(a)
                #print result
                
            #print "answer =", solution.reverse()
            #print "parent_dict -", parent_dict
            #print "explored-", explored
            #print "result-", result
            return result
                #mine.append(e[1])
            
            break
        
        # expand the next node(its state in particular) if not the goal node
        #if counter > 0 and nxt not in explored:
            #(nxt, action, cost) = choice_node
        if nxt not in explored: 
            successors = problem.getSuccessors(nxt)
            explored.add(nxt)
  
            for elem in successors:
                #h = heuristic(successors[0], problem)
                if problem.isGoalState(elem[0]):
                    goal_states.append(elem)
                    parent_dict[elem] = nxt
            
            for elem in successors:
    
                #nxt, action, cost = elem
                if elem[0] not in explored:
                    #h = heuristic(next_state, problem)
                    frontier.push(elem, (elem[2]) + costSoFar[nxt] + heuristic(elem[0], problem))
                    parent_dict[elem] = nxt
                
                
            #explored.add(elem)
        counter += 1       
        #frontier.get_frontier()
        #sleep(0.1)
    return None 
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch






