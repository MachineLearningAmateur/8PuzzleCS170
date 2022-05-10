import copy #import copy to use deepcopy since Python arguments are pass by reference
import numpy as np #imports np for random generator
from Node import Node #imports the Node class

class GreedyAlgs:
    def __init__(self, features : int, algorithm : int):
        self.features = features
        self.algorithm = algorithm
        self.bwAccuracy = None #best or worst accuracy in n features
        self.fSet = set() #empty feature set for best feature set
        self.bSubsets = {} #empty dictionary for best subsets found 
        self.bwSet = -1 #

    def begin(self):
        print("Beginning Search.\n")
        if self.algorithm == 1:
            self.forward_selection()
        elif self.algorithm == 2:
            self.backward_selection()
        else:
            self.personal_alg()
        return

    def dummyEval(self, node : Node): 
        #https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
        #perform eval function on node, and then return a random %
        return (np.random.random() * 100) #returns a random float 

    def forward_selection(self): #forward selection starts with an empty set
        # print('Do forward selection.')
        for to_iterate in range(self.features): #just need to iterate n times, where n = number of features
            self.bwAccuracy = 0
            bFeature = None
            for subset in range(1, self.features + 1): #start from 1 to the number of features present
                if subset not in self.fSet: #checks to see if we made the subset already ~ if we did, then skip
                    currNode = Node(copy.deepcopy(self.fSet))
                    currNode.addToSet(subset)
                    accuracy = self.dummyEval(currNode)
                    currNode.displayResults(accuracy)
                    if (self.bwAccuracy < accuracy): #checks if current accuracy is better than bwAccuracy (basically checking for max)
                        self.bwAccuracy = accuracy
                        bFeature = currNode
                        bwSet = subset
            print()
            bFeature.displayBest()
            self.fSet.add(bwSet)
            self.bSubsets[bFeature.accuracy] = bFeature.subset #use accuracy to store as key and the value is the best subset for current iteration
        #use max to find the highest accuracy within the keys of bSubsets
        print(f'Finished Search!!! The best feature subset is {self.bSubsets[max(self.bSubsets.keys())]}, which has an ' + \
            f'accuracy of {max(self.bSubsets.keys())}%')

    def backward_selection(self): #backward selection starts with a populated set
        print('Do backward selection.')
        for set in range(1, self.features + 1): #populate the set with the given number of features
            self.fSet.add(set)
        
        currNode = Node(copy.deepcopy(self.fSet))
        accuracy = self.dummyEval(currNode)
        currNode.displayResults(accuracy)
        currNode.displayBest()
        self.bSubsets[currNode.accuracy] = currNode.subset

        for to_iterate in range(self.features - 1): #-1 because we did a check for the full set already
            self.bwAccuracy = 0 
            bFeature = None
            for subset in range(1, self.features + 1):
                if subset in self.fSet:
                    currNode = Node(copy.deepcopy(self.fSet))
                    currNode.removeFromSet(subset)
                    accuracy = self.dummyEval(currNode)
                    currNode.displayResults(accuracy)
                    if (self.bwAccuracy < accuracy):
                        self.bwAccuracy = accuracy
                        bFeature = currNode
                        bwSet = subset
            print()
            bFeature.displayBest()
            self.fSet.remove(bwSet)
            self.bSubsets[bFeature.accuracy] = bFeature.subset #use accuracy to store as key and the value is the best subset for current iteration
        print(f'Finished Search!!! The best feature subset is {self.bSubsets[max(self.bSubsets.keys())]}, which has an ' + \
            f'accuracy of {max(self.bSubsets.keys())}%')

    def personal_alg(self): #possibly use bi-directional greedy best search?
        print('personal alg')
    
    def leave_one_out(self, node : Node):
        print('To be implemented for part 2...')
    
