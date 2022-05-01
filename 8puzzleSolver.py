from problem import Problem #imports the problem class
from searchAlgo import SearchAlgo #imports the searchAlgo class

def main():
    print("Welcome to jzhan326's eight puzzle solver!")
    
    choice = input('Type "1" to use a default puzzle, or "2" to enter your own puzzle: ')

    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #we can modify goal state as needed, but for now it's hard coded

    while (choice  != '1' and choice != '2'):
        choice = input('Please choose a valid choice. Either "1" for default or "2" to enter your own puzzle. ')
        
    if (choice == '1'):
        #3 by 3 matrix for the puzzle layout
        eight_puzzle = [[1, 2, 3], [4, 0, 5], [6, 7, 8]] #initial state pulled from the reading 
    else: #case for choice == '2'
        print('Enter your puzzle, use a zero to represent the blank.')
        row1 = input('Enter the first row, use space or tabs between numbers. ')
        row2 = input('Enter the second row, use space or tabs between numbers. ')
        row3 = input('Enter the third row, use space or tabs between numbers. ')

        #will set each row to be a list of the numbers inputted and convert each to int and make a list out of it
        row1 = list(map(int, row1.split())) #default separator is whitespace
        row2 = list(map(int, row2.split())) 
        row3 = list(map(int, row3.split()))

        #creates a list containing row1 - row3
        eight_puzzle = [row1, row2, row3] 
    
    givenProblem = Problem(eight_puzzle, goal_state) #initialize the problem with initial_state and goal_state
    givenProblem.printProblem() #display the problem to console
    givenProblem.findStart() #need to set the starting point for the given problem

    algo = input("""Enter your choice of algorithm \n
    1. Uniform Cost Search \n
    2. A* with the Misplaced Tile heuristic \n
    3. A* with the Euclidean distance heuristic.\n""")

    #keeps looping until a valid answer is inputted.
    while (algo != '1' and algo != '2' and algo != '3'):
        algo = input("""Enter your choice of algorithm \n
    1. Uniform Cost Search \n
    2. A* with the Misplaced Tile heuristic \n
    3. A* with the Euclidean distance heuristic.\n""")

    print()
    solver = SearchAlgo(givenProblem, algo)
    solver.solve() 
    
if __name__ == "__main__": #when interpreter runs this module, it will be set as main and we want main() to be called
    main()