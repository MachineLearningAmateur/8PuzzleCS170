from problem import Problem

class SearchAlgo:
    def __init__(self, problem : Problem, algorithm):
        self.problem = problem
        self.algorithm = algorithm
        self.expanded = 0
        self.maxNodes = 0
        self.depth = 0

    def solve(self):
        print("solve the problem")
        

    def uniformCostSearch(self):
        print("does uniformCostSearch")
    
    
    def results(self):
        print('Goal!!\n')
        print(f'To solve this problem the search algorithm expanded a total of {self.expanded} nodes.')
        print(f'The maximum number of nodes in the queue at any one time: {self.maxNodes}.')
        print(f'The depth of the goal node was {self.depth}.')



        