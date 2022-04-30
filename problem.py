from typing import List #to explicitly label list[list] for initial and goal states


class Problem: 
    def __init__(self, initial_state : List[List], goal_state : List[List]):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def printProblem(self):
        print("This is the state of the eight puzzle: ")
        print()
        for row in self.initial_state:
            print(row)
        print()


