from Classifier import Classifier
from Node import Node

class Validator:
    def __init__(self, subset : Node, classifier : Classifier):
        self.subset = subset
        self.classifier = classifier
        self.accuracy = None

    def validate(self): #creates the list that will be used to pass into the classifier for testing
        #might need a deepcopy here
        validatedList = []
        # print(self.subset.subset)
        for row in range(len(self.classifier.content)):
            tempRow = [] 
            for feature in self.subset.subset:
                tempRow.append(self.classifier.content[row][feature])
            validatedList.append(tempRow)
        self.classifier.test(validatedList)
        self.accuracy = self.classifier.accuracy
        # print(validatedList)

    def getAccuracy(self):
        return self.accuracy