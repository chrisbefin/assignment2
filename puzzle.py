#!usr/bin/env python

import argparse
from time import perf_counter
import multiprocessing
from multiprocessing.pool import Pool
from multiprocessing import cpu_count
import numpy as np

class Puzzle_MP(object):
    """ This class handles all stages of solving the Vietnamese puzzle. It iterates over possible solutions, identifies solutions and then writes those solutions to an output file using a multiprocessing strategy. Solutions using arithmetic order of operations and sequential execution of operations are both identifed.
    data members:
        solutions: a list of lists, where each inner list is a solution to the Vietnamese puzzle<2D list>
        processCount: the number of logical processing cores available on the executing machine<int>
        outputFile: the path to the file where solutions will be written<string>
        num_solutions: tracks the number of found solutions <int>
        numbers: range of possible ints for permuations <range object>
    methods:
        init(): initializes data members and calls the class methods necessary to find and record all solutions
        run(): creates a process pool, provides tasks for the pool to execute and retrieves results of the executed tasks
        permutation(): recursive method which finds all permutations of a given list with constraints
        find_solutions(): checks permutations provided by permutation() method for both sequential and PEMDAS solutions
        write(): writes all solutions to the given output file
    """
    def __init__(self, outputFile, start, end):
        """ initializes data members and calls the class methods necessary to find and record all solutions
            arguments: outputFile<string>, start <int>, end<int>
            returns: None
        """
        self.solutions = []
        self.processCount = cpu_count()
        self.outputFile = outputFile
        self.num_solutions = 0
        self.numbers = range(start, end+1)

        self.run() # find solutions using multiprocessing
        self.write() # write solutions to output file

    def permutation(self, _list, start, end, flag):
        """ generates a list of all possible permutations of the input list with first digit in the inclusive range of start-end. When this method is first called, flag should be set to True
            arguments: list to be permuted<list of ints>, start<int>, end<int>, flag<bool>
            returns: list of int lists containing permutations
        """
        # base cases
        if len(_list) == 0: # empty list has no permutations
            return []
        if len(_list) == 1: # one element has just one permutation
            return [_list]

        results = [] # empty list that will store permutations

        if flag == True: # flag is only True on first run
            values = range(start-1,end) # limits the values for the first number in the permutation
        else:
            values = range(len(_list)) # every subsequent recuvrsive run can choose from the full list of possibilities

        for value in values: # iterate over possible values and recursively build up all possible permutations
            next_value = _list[value]
            remList = _list[:value] + _list[value+1:] # remove list[i] from the list
            for perm in self.permutation(remList, start, end, False): # recursive call to permutation method
                results.append([next_value] + perm) # build all permutations with m as the first element
        return results

    def run(self):
        """ creates a process pool, provides tasks for the pool to execute and retrieves results of the executed tasks
            arguments: None
            returns: None
        """
        processList = [] # list of spawned processes
        chunks = np.array_split(range(1,10), self.processCount) # divide work into even chunks
        with Pool(processes=self.processCount) as pool: # create a process pool of size processCount
            for chunk in chunks:
                processList.append(pool.apply_async(self.find_solutions, args=(chunk[0],chunk[-1], list(self.numbers)))) # create a process for each chunk

            for process in processList: # for each process
                outputValue, temp = process.get() # retrieve return value and found solutions from the executed process
                self.num_solutions += temp # update found solutions
                self.solutions.extend(outputValue) # add to the solution list


    def find_solutions(self, start, end, numbers):
        """ This function finds all sequential and PEMDAS solutions to the Vietnamese puzzle by checking permutations provided by the permutation() method with the first number being in the range start-end. Upon completion, a summary is printed to terminal specifying the number of solutions found and the time taken.
            arguments:
                start: <int> the beginning of the range of values for the first number that the function will evaluate
                end: <int> the end of the range of values for the first number that the function will evaluate
                numbers: <list of ints> list that is to be permuted off of
            returns: list of solutions <list of lists of ints>
        """
        time_start = perf_counter() # begin timer
        num_solutions = 0 # number of solutions
        total_checks = 0 # number of possibilities checked
        solutions = [] # list of solutions

        options = self.permutation(numbers, start, end, True) # get permutations with contraints
        for x1,x2,x3,x4,x5,x6,x7,x8,x9 in options:
            total_checks += 1 # increment the number of checks performed
            if (((((((((((((x1+13)*x2)/x3)+x4)+12)*x5)-x6)-11)+x7)*x8)/x9)-10) == 66.0000): # check to see if this solution is valid
                num_solutions += 1 # increment the number of solutions
                solutions.append(['Sequential',x1,x2,x3,x4,x5,x6,x7,x8,x9]) # append valid solution to the list of solutions
            if (x1+13*x2/x3+x4+12*x5-x6-11+x7*x8/x9-10 == 66.0000): # check if this combo is a valid solution
                num_solutions += 1 # increment number of discovered solutions
                solutions.append(['PEMDAS',x1,x2,x3,x4,x5,x6,x7,x8,x9]) # add the solution to the list of solutions

        time_end = perf_counter() # time end
        print("{} checks performed and {} total solutions found in {} seconds".format(total_checks, num_solutions, time_end-time_start)) # print summary to terminal
        return solutions, num_solutions

    def write(self):
        """ writes all solutions to the given output file
            arguments: none
            returns: None
            **an S at the beginning of the line indicates it is a sequential solution, an O at the beginning of the line indicates it is an order of operations solution.
        """
        with open(self.outputFile, mode='w') as WRITE_FILE: # contextually open the user specified output file
            WRITE_FILE.write("{} total solutions discovered\n".format(self.num_solutions))
            for solution in self.solutions:
                WRITE_FILE.write("{}\n".format(str(solution).strip('[]'))) # write all solutions to the file
        print("{} total solutions discovered".format(self.num_solutions))

def main():
    """ parses user input for the creation of a Puzzle_MP object, which will solve the Vietnamese puzzle. This function also times the total execution of the program, including argument parsing and writing output to file and prints the result before exiting.
        arguments: None
        returns: None
    """
    start = perf_counter() # time start
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="path to the file that solutions will be written to")
    parser.add_argument("start", help="value from which permuations will start")
    parser.add_argument("end", help="value from which permutations will end")
    args = parser.parse_args() # parse command line arguments
    outputFile = args.output
    start_value = int(args.start)
    end_value = int(args.end)

    Puzzle_MP(outputFile, start_value, end_value) # create oject which will solve the puzzle

    end = perf_counter() # time end
    print("Time taken: {}".format(end-start)) # print timing summary to terminal

if __name__ == "__main__":
    main()
