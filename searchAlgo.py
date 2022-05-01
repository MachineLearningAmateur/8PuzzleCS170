from problem import Problem
from typing import List #to explicitly label list[list] for initial and goal states
from copy import deepcopy
import time #used to produce stats for the search algorithms


#Node handles the Problem, depth, heuristic cost, and expanded boolean
#Node has pointesr for 4 possible states (top, bot, left, right) that can be entered from current location of 0 in the problem
class Node:
    def __init__(self, problem : Problem):
        self.problem = problem  
        self.depth = 0
        self.hCost = 0
        self.expanded = False
        self.top = None
        self.bot = None
        self.left = None
        self.right = None

class SearchAlgo:
    def __init__(self, problem : Problem, algorithm : str):
        #_ is used to emulate private variables
        self.problem = problem
        self.algorithm = int(algorithm)
        self._maxNodesQ = 0
        self._depth = 0
        self._nodesExpanded = -1 #-1 to offset the first expansion
        
    def solve(self):
        self.graphSearch(self.problem)

    #graph search is our main driver 
    def graphSearch(self, problem):
        frontier = [] #frontier will be used as a queue (first in first out)
        visited = set() #a set is best because it prevents duplicates
        frontierSize = 0 #tracks the size of frontier
        
        if (self.algorithm == 1):
            heuristic = 0
        elif (self.algorithm == 2):
            heuristic = self.MisplacedTileA(problem)
        elif (self.algorithm == 3):
            heuristic = self.EuclidianDistance(problem)
        
        state = Node(problem)
        state.hCost = heuristic
        state.depth = 0

        frontier.append(state) #add this node as a possible state to our frontier


        while frontier: #keeps running the loop while frontier is full, we will add a case to terminate loop if goal state is found
            #need to sort frontier which has a list of objects 
            #https://www.techiedelight.com/sort-list-of-objects-python/
            #used the link above for inspiration to properly sort a list of objects based on the members

            if (self.algorithm == 1): #for uniform cost search we need the g(n) to be on top of the queue/frontier
                frontier.sort(key = lambda x : x.depth)
                #print('UFC')

            currNode = frontier.pop(0) #access the top of the queue or end of the list since python does not have a queue data structure
            frontierSize = len(frontier) #update size of frontier
            if currNode.problem.checkGoal():
                self._depth = currNode.depth
                self.results()
                return

            if not currNode.expanded:
                self._nodesExpanded += 1 #add 1 cause we will expand this node
                currNode.expanded = True #make sure it's true so we won't expand a state that has already been explored
                

            if self._nodesExpanded != 0:
                print(f'The best state to expand with a g(n) = {currNode.depth} and h(n) = {currNode.hCost} is...\n')
                currNode.problem.printProblem()
                print(currNode.problem.start)
            else:
                currNode.problem.printProblem()
            
            currNode = self.domainExpansion(currNode, visited) #time to expand the states for the given state
            print(len(visited))
            #check to see if the states expanded are visited or not
            for state in [currNode.top, currNode.bot, currNode.left, currNode.right]:
                print(state)
                if state: #if state = None it would return false
                    if (self.algorithm == 1): #ufc case
                        state.hCost = 0
                        state.depth = currNode.depth + 1
                    elif (self.algorithm == 2): #misplaced case
                        state.hCost = 0 #need to fix this
                        state.depth = currNode.depth + 1
                    elif (self.algorithm == 3): #euclidean distance case
                        state.hCost = 0 #need to fix this
                        state.depth = currNode.depth + 1
                    
                    frontier.append(state)
                    # state.problem.printProblem()
                    # print(state.problem.start)
                    visited.add(tuple(tuple(row) for row in state.problem.initial_state))
                    #frontierSize += 1

            self._maxNodesQ = max(frontierSize, self._maxNodesQ) #update maxNodesQ is frontierSize is larger than what's currently stored
         

    
    #used to explore the possible routes that 0 can be moved within the puzzle
    def domainExpansion(self, currNode : Node, visited : set):
        puzzle = currNode.problem
        row, col = puzzle.start
            
        for i in range(len(puzzle.operators) - 1):
            newRow, newCol = puzzle.operators[i] + row, puzzle.operators[i + 1] + col
            if newRow < 0 or newRow >= len(puzzle.initial_state) or newCol < 0 or newCol >= len(puzzle.initial_state[0]):
                continue
            #creates the problem to be used, we use a deepcopy to make sure that the references are unique
            tempPuzzle = self.createProblem(deepcopy(puzzle.initial_state), puzzle.goal_state)
            tempPuzzle.update(row, col, newRow, newCol) #swaps the value at the curr index with the value at the moved index
            
            #if the initial state already exists in visited we just skip it
            checker = tuple(tuple(row) for row in tempPuzzle.initial_state)
            if checker in visited:
                print('seen!')
                continue
            tempPuzzle.findStart()
            tempNode = Node(tempPuzzle)
            
            if i == 0:
                currNode.bot = tempNode
            if i == 1:
                currNode.left = tempNode
            if i == 2:
                currNode.top = tempNode
            if i ==3:
                currNode.right = tempNode

            tempNode.problem.printProblem()
            print(tempNode.problem.start)
        print("domainExpansion")
        return currNode

    def createProblem(self, initial : List[List], goal : List[List]):
        problemCreated = Problem(initial, goal)
        return problemCreated

    def MisplacedTileA(self, problem : Problem):
        print("perform A* with the Misplaced Tile heuristic.")

    def EuclidianDistance(self, problem : Problem):
        print("perform A* with the Euclidean Distance heuristic")

    def results(self):
        print('Goal!!\n')
        print(f'To solve this problem the search algorithm expanded a total of {self._nodesExpanded} nodes.')
        print(f'The maximum number of nodes in the queue at any one time: {self._maxNodesQ}.')
        print(f'The depth of the goal node was {self._depth}.')

