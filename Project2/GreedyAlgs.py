import copy
import numpy as np
from Node import Node

class GreedyAlgs:
    def __init__(self, features : int, algorithm : int):
        self.features = features
        self.algorithm = algorithm
        self.bAccuracy = None
        self.fSet = set() #empty feature set for best feature set
        self.bSubset = {} #empty dictionary for best subset found 
        self.choices = []

    def begin(self):
        print("Beginning Search.\n")
        self.generateChoices()
        if self.algorithm == 1:
            self.forward_selection()
        elif self.algorithm == 2:
            self.backward_selection()
        else:
            print('Personal Algorithm')
        return

    def generateChoices(self):
        #print('Generate choices.')
        for i in range(1, self.features + 1):
            self.choices.append(i)
        print(str(self.choices) + '\n')
        return 

    def dummyEval(self, node : Node):
        #https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
        #perform eval function on node, and then return a random %
        return (np.random.random() * 100) #returns a random float 

    def forward_selection(self):
        # print('Do forward selection.')
        for to_iterate in range(self.features):
            self.bAccuracy = 0
            bFeature = None
            for subset in self.choices:
                if subset not in self.fSet:
                    currNode = Node(copy.deepcopy(self.fSet))
                    currNode.addToSet(subset)
                    accuracy = self.dummyEval(currNode)
                    currNode.displayResults(accuracy)
                    if (self.bAccuracy < accuracy):
                        self.bAccuracy = accuracy
                        bFeature = currNode
                        bSet = subset
            print()
            bFeature.displayBest()
            self.fSet.add(bSet)
            self.bSubset[bFeature.accuracy] = bFeature.subset #use accuracy to store as key and the value is the best subset for current iteration
        print(f'Finished Search!!! The best feature subset is {self.bSubset[max(self.bSubset.keys())]}, which has an ' + \
            f'accuracy of {max(self.bSubset.keys())}%')


    def backward_selection(self):
        print('Do backward selection.')

    def leave_one_out(self):
        print('To be implemented...')
    