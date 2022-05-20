from Classifier import Classifier
from Node import Node

class Validator:
    def __init__(self, subset : Node, classifier : Classifier):
        self.subset = subset
        self.classifier = classifier
    
    def createList(): #creates the list that will be used to pass into the classifier
        print('create list')