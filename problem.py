from typing import List #to explicitly label list[list] for initial and goal states


class Problem: 
    def __init__(self, initial_state : List[List], goal_state : List[List]):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.operators = [1, 0, -1, 0, 1] #ultimate cheat code for matrix traversal
        self.start = [0, 0] #starting point

    def findStart(self):
        for row in range(len(self.initial_state)):
            for col in range(len(self.initial_state[row])):
                if self.initial_state[row][col] == 0:
                    self.start = [row, col]
        #print(self.start)

    def printProblem(self):
        print("Expanding state:\n")
        for row in self.initial_state:
            print(row)
        print()

    def update(self, row1, col1, row2, col2):
        #swaps the val at row1, col1 with the val at row2, col2 vice versa
        print(self.initial_state[row1][col1])
        print(self.initial_state[row2][col2])
        self.initial_state[row1][col1], self.initial_state[row2][col2] = self.initial_state[row2][col2], self.initial_state[row1][col1]

    def checkGoal(self):
        if self.initial_state == self.goal_state:
            return True
        else: 
            return False

