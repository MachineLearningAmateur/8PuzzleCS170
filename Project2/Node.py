class Node:
    def __init__(self, subset):
        self.subset = subset #stores the current subset
        self.accuracy = None

    def displayResults(self, accuracy : float):
        #https://www.w3schools.com/python/ref_func_round.asp
        self.accuracy = round(accuracy * 100, 2)
        return (f'Using feature(s) {self.subset} is {self.accuracy}%')

    def addToSet(self, val): #for forward selection
        self.subset.add(val)

    def removeFromSet(self, val): #for backward selection
        self.subset.remove(val)

    def displayBest(self):
        return (f'Feature set {self.subset} was best, accuracy is {self.accuracy}%\n')