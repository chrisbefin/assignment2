import argparse
from time import perf_counter
import multiprocessing
from multiprocessing.pool import Pool
from multiprocessing import cpu_count

class Puzzle_MP(object):
    """ This class handles all stages of solving the Vietnamese puzzle. It iterates over possible solutions, identifies solutions and then writes those solutions to an output file using a multiprocessing strategy. Solutions using arithmetic order of operations and sequential execution of operations are both identifed.
    data members:
        solutions: a list of lists, where each inner list is a solution to the Vietnamese puzzle<2D list>
        processCount: the number of logical processing cores available on the executing machine<int>
        outputFile: the path to the file where solutions will be written<string>
    methods:
        init(): initializes data members and calls the class methods necessary to find and record all solutions
        run(): creates a process pool, provides tasks for the pool to execute and retrieves results of the executed tasks
        pemdas(): finds solutions to the Vietnamese puzzle using standard arithmetic order of operations
        sequential(): finds solutions to the Vietnamese puzzle using sequential execution of arithmetic operations
        write(): writes all solutions to the given output file
    """
    def __init__(self, outputFile):
        """ initializes data members and calls the class methods necessary to find and record all solutions
            arguments: self, outputFile<string>
            returns: None
        """
        self.solutions = []
        self.processCount = cpu_count()
        self.outputFile = outputFile

        self.run() # find solutions using multiprocessing
        self.write() # write solutions to output file

    def run(self):
        """ creates a process pool, provides tasks for the pool to execute and retrieves results of the executed tasks
            arguments: self
            returns: None
        """
        processList = [] # list of spawned processes
        with Pool(processes=self.processCount) as pool: # contextually create a process pool of size processCount
            processList.append(pool.apply_async(self.pemdas, args=(1,5))) # create processes
            processList.append(pool.apply_async(self.pemdas, args=(6,9)))
            processList.append(pool.apply_async(self.sequential, args=(1,5)))
            processList.append(pool.apply_async(self.sequential, args=(6,9)))
            for process in processList: # for each process
                outputValue = process.get() # retrieve return value from the executed process
                self.solutions.extend(outputValue) # add to the solution list

    def pemdas(self, start, end):
        """ This function finds all PEMDAS solutions to the Vietnamese puzzle by iterating all possible numbers with the first number being in the range start-end. Upon completion, a summary is printed to terminal specifying the number of solutions found and the time taken.
            arguments:
                start: <int> the beginning of the range of values for the first number that the function will evaluate
                end: <int> the end of the range of values for the first number that the function will evaluate
            returns: list of solutions <list>
        """
        time_start = perf_counter() # begin timer
        starting_numbers = list(range(start,end+1))
        solutions = [] # list of solutions
        num_solutions = 0 # number of solutions discovered
        total_checks = 0 # number of combinations checked

        # the first value iterates over all possibilities specified by the start and end arguments
        # each subsequent for loop represents the next variable in the puzzle
        # since all variables must be unique integers, the options to choose from are reduced by 1 each loop until you arrive at the final loop, with only one possible number
        for x2 in starting_numbers:
            options = [1,2,3,4,5,6,7,8,9]
            options.remove(x2) # reduce options by 1
            x3_options = options.copy()
            for x3 in x3_options:
                x7_options = x3_options.copy()
                x7_options.remove(x3) # reduce options by 1
                for x7 in x7_options:
                    x8_options = x7_options.copy()
                    x8_options.remove(x7) # reduce options by 1
                    for x8 in x8_options:
                        x9_options = x8_options.copy()
                        x9_options.remove(x8) # reduce options by 1
                        for x9 in x9_options:
                            x6_options = x9_options.copy()
                            x6_options.remove(x9) # reduce options by 1
                            for x6 in x6_options:
                                x1_options = x6_options.copy()
                                x1_options.remove(x6) # reduce options by 1
                                for x1 in x1_options:
                                    x4_options = x1_options.copy()
                                    x4_options.remove(x1) # reduce options by 1
                                    for x4 in x4_options:
                                        x5_options = x4_options.copy()
                                        x5_options.remove(x4) # reduce options by 1
                                        for x5 in x5_options:
                                            total_checks += 1 # increment number of combos checked
                                            if (x1+13*x2/x3+x4+12*x5-x6-11+x7*x8/x9-10 == 66.0000): # check if this combo is a valid solution
                                                num_solutions += 1 # increment number of discovered solutions
                                                solutions.append(['O',x1,x2,x3,x4,x5,x6,x7,x8,x9]) # add the solution to the list of solutions
        time_end = perf_counter()
        print("{} checks performed and {} PEMDAS solutions found in {} seconds".format(total_checks, num_solutions, time_end-time_start)) # print summary to the terminal
        return solutions

    def sequential(self, start, end):
        """ This function finds all sequential solutions to the Vietnamese puzzle by iterating all possible numbers with the first number being in the range start-end. Upon completion, a summary is printed to terminal specifying the number of solutions found and the time taken.
            arguments:
                start: <int> the beginning of the range of values for the first number that the function will evaluate
                end: <int> the end of the range of values for the first number that the function will evaluate
            returns: list of solutions <list>
        """
        time_start = perf_counter() # begin timer
        starting_numbers = list(range(start,end+1))
        num_solutions = 0 # number of solutions
        total_checks = 0 # number of possibilities checked
        solutions = [] # list of solutions

        # the first value iterates over all possibilities specified by the start and end arguments
        # each subsequent for loop represents the next variable in the puzzle
        # since all variables must be unique integers, the options to choose from are reduced by 1 each loop until you arrive at the final loop, with only one possible number
        for x2 in starting_numbers:
            options = [1,2,3,4,5,6,7,8,9]
            options.remove(x2) # reduce options by 1
            x3_options = options.copy()
            for x3 in x3_options:
                x7_options = x3_options.copy()
                x7_options.remove(x3) # reduce options by 1
                for x7 in x7_options:
                    x8_options = x7_options.copy()
                    x8_options.remove(x7) # reduce options by 1
                    for x8 in x8_options:
                        x9_options = x8_options.copy()
                        x9_options.remove(x8) # reduce options by 1
                        for x9 in x9_options:
                            x6_options = x9_options.copy()
                            x6_options.remove(x9) # reduce options by 1
                            for x6 in x6_options:
                                x1_options = x6_options.copy()
                                x1_options.remove(x6) # reduce options by 1
                                for x1 in x1_options:
                                    x4_options = x1_options.copy()
                                    x4_options.remove(x1) # reduce options by 1
                                    for x4 in x4_options:
                                        x5_options = x4_options.copy()
                                        x5_options.remove(x4) # reduce options by 1
                                        for x5 in x5_options:
                                            total_checks += 1 # increment the number of checks performed
                                            if (((((((((((((x1+13)*x2)/x3)+x4)+12)*x5)-x6)-11)+x7)*x8)/x9)-10) == 66.0000): # check to see if this solution is valid
                                                num_solutions += 1 # increment the number of solutions
                                                solutions.append(['S',x1,x2,x3,x4,x5,x6,x7,x8,x9]) # append valid solution to the list of solutions
        time_end = perf_counter() # time end
        print("{} checks performed and {} sequential solutions found in {} seconds".format(total_checks, num_solutions, time_end-time_start)) # print summary to terminal
        return solutions

    def write(self):
        """ writes all solutions to the given output file
            arguments: self
            returns: None
            **an S at the beginning of the line indicates it is a sequential solution, an O at the beginning of the line indicates it is an order of operations solution.
        """
        with open(self.outputFile, mode='w') as WRITE_FILE: # contextually open the user specified output file
            for solution in self.solutions:
                WRITE_FILE.write("{}\n".format(solution)) # write all solutions to the file


def main():
    """ parses user input for the creation of a Puzzle_MP object, which will solve the Vietnamese puzzle. This function also times the total execution of the program, including argument parsing and writing output to file and prints the result before exiting.
        arguments: None
        returns: None
    """
    start = perf_counter() # time start
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="path to the file that solutions will be written to")
    args = parser.parse_args() # parse command line arguments
    outputFile = args.output

    Puzzle_MP(outputFile) # create oject which will solve the puzzle

    end = perf_counter() # time end
    print("Time taken: {}".format(end-start)) # print timing summary to terminal

if __name__ == "__main__":
    main()
