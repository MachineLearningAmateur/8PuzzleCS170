
from GreedyAlgs import GreedyAlgs #imports the GreedyAlgs class
import os

def main(): 
    print('Welcome to jzhan326\'s Feature Selection Algorithm.')
    #numFeatures = input('Please enter total number of features: ') 
    # while not numFeatures.isdigit():
    #     print('Please enter a valid integer.')
    #     numFeatures = input('Please enter total number of features: ') 
    fileName = input('Please enter name of the file: ').strip()
    while not os.path.isfile(fileName):
        fileName = input('Please enter a valid file name: ')
        
    algorithm = input('Type the number of the algorithm you want to run.\n' + \
    '\t* Forward Selection\n' + \
    '\t* Backward Elimination\n' + \
    '\t* James\' Special Algorithm\n')
    while algorithm != '1' and algorithm != '2' and algorithm != '3':
        print('Please enter a valid choice!')
        algorithm = input('Type the number of the algorithm you want to run.\n' + \
    '\t* Forward Selection\n' + \
    '\t* Backward Elimination\n' + \
    '\t* James\' Special Algorithm\n')

    # algs = GreedyAlgs(int(numFeatures), int(algorithm))

    algs = GreedyAlgs(fileName, int(algorithm))
    algs.begin()

if __name__ == '__main__':
    main()


