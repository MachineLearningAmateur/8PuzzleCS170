import copy #import copy to use deepcopy since Python arguments are pass by reference
import numpy as np #imports np for random generator
import time
import os
from Node import Node #imports the Node class
from Classifier import Classifier
from Validator import Validator

class GreedyAlgs:
    def __init__(self, fileName : int, algorithm : int):
        self.fileName = fileName
        self.features = 0
        self.algorithm = algorithm
        self.bAccuracy = None #best accuracy in n features
        self.fSet = set() #empty feature set for best feature set
        self.bSubsets = {} #empty dictionary for best subsets found 
        self.bwSet = -1 
        self.classifier = None
        self.validator = None

    def begin(self):
        print("Beginning Search.\n")
        #set up the classifier by passing in the fileName
        self.classifier = Classifier(self.fileName)
        self.classifier.train()
        self.features = self.classifier.features
        if os.path.isfile(self.fileName.replace('.txt', '') + '_trace.txt'):
            with open(self.fileName.replace('.txt', '') + '_trace.txt', 'r+') as f:
                    f.truncate(0) # need '0' when using r+
        if self.algorithm == 1:
            self.forward_selection()
        elif self.algorithm == 2:
            self.backward_elimination()
        else:
            self.personal_alg()
        return

    # def dummyEval(self, node : Node): 
    #     #https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
    #     #perform eval function on node, and then return a random %
    #     return (np.random.random() * 100) #returns a random float 

    def evaluate(self, node: Node):
        #might need deepcopy here?
        self.validator = Validator(node, self.classifier)
        self.validator.validate()
        accuracy = self.validator.getAccuracy()
        self.classifier.reset()
        return accuracy

    def forward_selection(self): #forward selection starts with an empty set
        # print('Do forward selection.')
        total = time.time() #tracks time for the whole selection
        for to_iterate in range(self.features): #just need to iterate n times, where n = number of features
            self.bAccuracy = -1
            bFeature = None
            start = time.time()
            for subset in range(1, self.features + 1): #start from 1 to the number of features present
                if subset not in self.fSet: #checks to see if we made the subset already ~ if we did, then skip
                    currNode = Node(copy.deepcopy(self.fSet))
                    currNode.addToSet(subset)
                    accuracy = self.evaluate(currNode)
                    self.trace(currNode.displayResults(accuracy), None)
                    print(currNode.displayResults(accuracy))
                    if (self.bAccuracy < accuracy): #checks if current accuracy is better than bAccuracy (basically checking for max)
                        self.bAccuracy = accuracy
                        bFeature = currNode
                        bwSet = subset
            print()
            self.trace(currNode.displayBest(), start)
            print(bFeature.displayBest())
            self.fSet.add(bwSet)
            decreasedAcc = False 
            for key in self.bSubsets.keys(): #check to see if best accuracy has decreased
                if (bFeature.accuracy < key):
                    decreasedAcc = True
                    break
            if (decreasedAcc):
                self.trace('(Warning, accuracy has decreased!)', None)
                print('(Warning, accuracy has decreased!)')
                break
            self.bSubsets[bFeature.accuracy] = bFeature.subset #use accuracy to store as key and the value is the best subset for current iteration
            
        #use max to find the highest accuracy within the keys of bSubsets
        self.trace(f'Finished Search!!! The best feature subset is {self.bSubsets[max(self.bSubsets.keys())]}, which has an ' + \
            f'accuracy of {max(self.bSubsets.keys())}%', total)
        print(f'Finished Search!!! The best feature subset is {self.bSubsets[max(self.bSubsets.keys())]}, which has an ' + \
            f'accuracy of {max(self.bSubsets.keys())}%')

    def backward_elimination(self): #backward selection starts with a populated set
        #print('Do backward elimination.')
        total = time.time()
        start = time.time()
        for set in range(1, self.features + 1): #populate the set with the given number of features
            self.fSet.add(set)
        
        currNode = Node(copy.deepcopy(self.fSet))
        accuracy = self.evaluate(currNode)
        self.trace(currNode.displayResults(accuracy), None)
        print(currNode.displayResults(accuracy))
        self.trace(currNode.displayBest(), start)
        print(currNode.displayBest())
        self.bSubsets[currNode.accuracy] = currNode.subset

        for to_iterate in range(self.features - 1): #-1 because we did a check for the full set already
            self.bAccuracy = -1 
            start = time.time()
            bFeature = None
            for subset in range(1, self.features + 1):
                if subset in self.fSet:
                    currNode = Node(copy.deepcopy(self.fSet))
                    currNode.removeFromSet(subset)
                    accuracy = self.evaluate(currNode)
                    self.trace(currNode.displayResults(accuracy), None)
                    print(currNode.displayResults(accuracy))
                    if (self.bAccuracy < accuracy):
                        self.bAccuracy = accuracy
                        bFeature = currNode
                        bwSet = subset
            print()
            self.trace(bFeature.displayBest(), start)
            print(bFeature.displayBest())
            self.fSet.remove(bwSet)
            decreasedAcc = False
            for key in self.bSubsets.keys(): #check to see if best accuracy has decreased
                if (bFeature.accuracy < key):
                    decreasedAcc = True
                    break
            if (decreasedAcc):
                self.trace('(Warning, accuracy has decreased!)', None)
                print('(Warning, accuracy has decreased!)')
                break
            self.bSubsets[bFeature.accuracy] = bFeature.subset #use accuracy to store as key and the value is the best subset for current iteration
        self.trace(f'Finished Search!!! The best feature subset is {self.bSubsets[max(self.bSubsets.keys())]}, which has an ' + \
            f'accuracy of {max(self.bSubsets.keys())}%', total)
        print(f'Finished Search!!! The best feature subset is {self.bSubsets[max(self.bSubsets.keys())]}, which has an ' + \
            f'accuracy of {max(self.bSubsets.keys())}%')

    def trace(self, text, start):
        with open(self.fileName.replace('.txt', '') + '_trace.txt', 'a') as f:
            if start:
                end = time.time() - start
                f.write(text.strip() + ' | step finished in ' + str(end) + ' seconds.' + '\n')
            else:
                f.write(text.strip() + '\n')
            
    def personal_alg(self): #possibly use bi-directional greedy best search?
        print('personal alg')
    
    
