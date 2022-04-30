from problem import Problem
import time #used to produce stats for the search algorithms

class SearchAlgo:
    def __init__(self, problem : Problem, algorithm : int):
        #_ is used to emulate private variables
        self.problem = problem
        self.algorithm = algorithm
        self._expanded = 0
        self._maxNodes = 0
        self._depth = 0

    def solve(self):
        if (self.algorithm == 1):
            self.uniformCostSearch()
        elif (self.algorithm == 2):
            self.MisplacedTileA()
        else:
            self.EuclidianDistance()

    def uniformCostSearch(self):
        print("perform Uniform Cost Search.")

    
    def MisplacedTileA(self):
        print("perform A* with the Misplaced Tile heuristic.")

    def EuclidianDistance(self):
        print("perform A* with the Euclidean Distance heuristic")
    def results(self):
        print('Goal!!\n')
        print(f'To solve this problem the search algorithm expanded a total of {self._expanded} nodes.')
        print(f'The maximum number of nodes in the queue at any one time: {self._maxNodes}.')
        print(f'The depth of the goal node was {self._depth}.')


#Node handles the Problem, depth, heuristic cost, and visited boolean
class node:
    def __init__(self, problem : Problem):
        self.problem = problem  
        self.depth = 0
        self.hCost = 0
        self.visited = False