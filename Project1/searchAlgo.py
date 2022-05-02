from problem import Problem
from typing import List #to explicitly label list[list] for initial and goal states
from copy import deepcopy
import time #used to produce stats for the search algorithms
import math #used to calculate euclidean distance



#Node handles the Problem, depth, heuristic cost, and expanded boolean
#Node has pointesr for 4 possible states (top, bot, left, right) that can be entered from current location of 0 in the problem
class Node:
    def __init__(self, problem : Problem):
        self.problem = problem  
        self.depth = 0
        self.hCost = 0
  
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
        self._nodesExpanded = 0 #-1 to offset the first expansion
    
    #to encapsulate our input we just call solve for convenience
    def solve(self):
        #we want to time our program to terminate after a certain duration
        startTime = time.time()
        self.graphSearch(self.problem)

    #graph search is our main driver code to create the frontier and call the expansion function
    def graphSearch(self, problem):
        frontier = [] #frontier will be used as a queue (first in first out)
        visited = set() #a set is best because it prevents duplicates
        frontierSize = 0 #tracks the size of frontier
        
        if (self.algorithm == 1):
            heuristic = 0
        elif (self.algorithm == 2):
            heuristic = self.MisplacedTileA(problem)
        elif (self.algorithm == 3):
            heuristic = self.EuclideanDistance(problem)
        
        state = Node(problem)
        state.hCost = heuristic
        state.depth = 0

        frontier.append(state) #add this node as a possible state to our frontier


        while frontier: #keeps running the loop while frontier is full, we will add a case to terminate loop if goal state is found

            #need to sort frontier which has a list of objects 
            #https://www.techiedelight.com/sort-list-of-objects-python/
            #used the link above for inspiration to properly sort a list of objects based on the members
            if (self.algorithm == 1): #for uniform cost search we need the lowest g(n) to be on top of the queue/frontier; technically this line of code is unneeded
                frontier.sort(key = lambda x : x.depth)
            elif (self.algorithm == 2 or self.algorithm == 3): #for A* we sort by lowest g(n) + h(n)
                frontier.sort(key = lambda x : x.depth + x.hCost)

            currNode = frontier.pop(0) #access the top of the queue or end of the list since python does not have a queue data structure

            if currNode.problem.checkGoal():
                self._depth = currNode.depth
                self.results()
                return

            self.traceStates(currNode)
            # if self._nodesExpanded != 0: #we don't have a best state at 0
            #     print(f'The best state to expand with a g(n) = {currNode.depth} and h(n) = {currNode.hCost} is...\n')
            #     currNode.problem.printProblem()
            #     #print(currNode.problem.start)
            # else:
            #     currNode.problem.printProblem()
            
            currNode = self.domainExpansion(currNode, visited) #time to expand the states for the given state
            self._nodesExpanded += 1 #add 1 to count whenever we call domainExpansion
            #print(len(visited))
            #check to see if the states are valid, and if valid we update their hcost and depth values
            for state in [currNode.top, currNode.bot, currNode.left, currNode.right]:
                #print(state)
                if state: #if state = None it would return false
                    if (self.algorithm == 1): #ufc case
                        state.hCost = 0
                        state.depth = currNode.depth + 1
                    elif (self.algorithm == 2): #misplaced case
                        state.hCost = self.MisplacedTileA(state.problem)
                        state.depth = currNode.depth + 1
                    elif (self.algorithm == 3): #euclidean distance case
                        state.hCost = self.EuclideanDistance(state.problem)
                        state.depth = currNode.depth + 1
                    
                    frontier.append(state)
                    # state.problem.printProblem()
                    # print(state.problem.start)
                    visited.add(tuple(tuple(row) for row in state.problem.initial_state))

            frontierSize = len(frontier) #update size of frontier 
            self._maxNodesQ = max(frontierSize, self._maxNodesQ) #update maxNodesQ if frontierSize is larger than what's currently stored

         

    
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
                #print('seen!')
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

        #print("domainExpansion")
        return currNode

    def createProblem(self, initial : List[List], goal : List[List]):
        problemCreated = Problem(initial, goal)
        return problemCreated

    #counts the number of misplaced tiles excluding 0 by comparing initial state to goal state
    def MisplacedTileA(self, problem : Problem):
        goal = problem.goal_state
        start = problem.initial_state #more of current state rather than initial
        counter = 0
        
        for row in range(len(start)):
            for col in range(len(start[0])):
                if start[row][col] != 0 and start[row][col] != goal[row][col]: 
                    counter += 1
        #misplaced refers to instances in which the position of numbers in initial_state do not match with the same position of numbers in goal_state
        return counter
        
    #takes the euclidean distance between the position of the number in the goal state compared to that of the position in the initial state
    def EuclideanDistance(self, problem : Problem): #https://byjus.com/maths/euclidean-distance/
        goal = problem.goal_state
        start = problem.initial_state
        counter = 0
        goalPtrRow, goalPtrCol, startPtrRow, startPtrCol = None, None, None, None

        #starts from 1 to 8
        for val in range(1, 9):
            for row in range(len(start)):
                for col in range(len(start)):
                    if (goal[row][col] == val): #once val is found in goal state store its position
                        goalPtrRow, goalPtrCol = row, col
                    if(start[row][col] == val): #once val is found in start state store its position
                        startPtrRow, startPtrCol, = row, col
            #counter is the sum of the total distance between each val in initial to their respective val in goal
            counter += math.sqrt(math.pow(goalPtrRow - startPtrRow, 2) + math.pow(goalPtrCol - startPtrCol, 2)) 

        return counter

    def results(self):
        print('Goal!!!\n')
        print(f'To solve this problem the search algorithm expanded a total of {self._nodesExpanded} nodes.')
        print(f'The maximum number of nodes in the queue at any one time: {self._maxNodesQ}.')
        print(f'The depth of the goal node was {self._depth}.')

        with open('tracedStates.txt', 'a') as file:
            file.write('Goal!!!\n' 
            + f'To solve this problem the search algorithm expanded a total of {self._nodesExpanded} nodes.\n' 
            + f'The maximum number of nodes in the queue at any one time: {self._maxNodesQ}.\n' 
            + f'The depth of the goal node was {self._depth}.')
    
    def traceStates(self, currNode):
        with open('tracedStates.txt', 'a') as file:

            if self._nodesExpanded != 0: #we don't have a best state at 0
                file.write(f'The best state to expand with a g(n) = {currNode.depth} and h(n) = {currNode.hCost} is...\n')
                file.write('Expanding state:\n\n')
                for row in currNode.problem.initial_state:
                    file.write(str(row) + '\n')
                file.write('\n')
                print(f'The best state to expand with a g(n) = {currNode.depth} and h(n) = {currNode.hCost} is...\n')
                currNode.problem.printProblem()
            
            else:
                file.write('Expanding state:\n\n')
                for row in currNode.problem.initial_state:
                    file.write(str(row) + '\n')
                file.write('\n')

