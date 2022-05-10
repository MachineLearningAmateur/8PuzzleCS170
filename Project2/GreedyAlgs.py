import numpy as np
from Node import Node

class GreedyAlgs:
    def __init__(self, features : int, algorithm : int):
        self.features = features
        self.algorithm = algorithm
        self.maxAccuracy = 0
        self.choices = []

    def begin(self):
        print("Beginning Search.")
        self.generateChoices()
        if self.algorithm == 1:
            print(self.forward_selection())
        elif self.algorithm == 2:
            print(self.backward_selection())
        else:
            print('Personal Algorithm')
        
    def generateChoices(self):
        print('Generate choices.')
        for i in range(1, self.features + 1):
            self.choices.append(i)
        print(self.choices)

    def dummyEval(self, node : Node):
        #https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
        #perform eval function on node, and then return a random %
        return np.random.random(0, 100) #returns a random float 

    def forward_selection(self):
        print('Do forward selection.')


    def backward_selection(self):
        print('Do backward selection.')
    