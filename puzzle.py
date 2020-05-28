import argparse
from time import perf_counter
import multiprocessing

def pemdas(fileName, start, end):
    """ This function finds all PEMDAS solutions to the Vietnamese puzzle by iterating all possible numbers with the first number being in the range start-end. Solutions are written to the specified output file. Upon completion, a summary is printed to terminal specifying the number of solutions found and the time taken.
        arguments:
            fileName: <string> the path to the file for solutions to be written to
            start: <int> the beginning of the range of values for the first number that the function will evaluate
            end: <int> the end of the range of values for the first number that the function will evaluate

    """
    time_start = perf_counter() # begin timer
    starting_numbers = list(range(start,end+1))
    num_solutions = 0 # number of solutions discovered
    solutions = [] # list of solutions
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
                                            solutions.append([x1,x2,x3,x4,x5,x6,x7,x8,x9]) # add the solution to the list of solutions
    with open(fileName, mode='a') as WRITE_FILE:
        WRITE_FILE.write("PEMDAS solutions: \n\n")
        for solution in solutions: # write every discovered solution to the specified output file
            WRITE_FILE.write("{}\n".format(solution))
        WRITE_FILE.write("\n")
    time_end = perf_counter()
    print("{} checks performed and {} PEMDAS solutions found and recorded in {} seconds".format(total_checks, num_solutions, time_end-time_start)) # print summary to the terminal


def sequential(fileName,start,end):
    """ This function finds all sequential solutions to the Vietnamese puzzle by iterating all possible numbers with the first number being in the range start-end. Solutions are written to the specified output file. Upon completion, a summary is printed to terminal specifying the number of solutions found and the time taken.
        arguments:
            fileName: <string> the path to the file for solutions to be written to
            start: <int> the beginning of the range of values for the first number that the function will evaluate
            end: <int> the end of the range of values for the first number that the function will evaluate

    """
    time_start = perf_counter() # begin timer
    solutions = [] #list of solutions
    starting_numbers = list(range(start,end+1))
    num_solutions = 0 # number of solutions
    total_checks = 0 # number of possibilities checked

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
                                            solutions.append([x1,x2,x3,x4,x5,x6,x7,x8,x9]) # append valid solution to the list of solutions
    with open(fileName, mode='a') as WRITE_FILE:
        WRITE_FILE.write("Sequential solutions: \n\n")
        for solution in solutions:
            WRITE_FILE.write("{}\n".format(solution)) # write all discovered solutions to the specified output file
        WRITE_FILE.write("\n")
    time_end = perf_counter() # time end
    print("{} checks performed and {} sequential solutions found and recorded in {} seconds".format(total_checks, num_solutions, time_end-time_start)) # print summary to terminal

def main():
    start = perf_counter()
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="path to the file that solutions will be written to")
    args = parser.parse_args() # parse command line arguments
    outputFile = args.output

    p1 = multiprocessing.Process(target=pemdas, args=(outputFile, 1, 9, ))
    p2 = multiprocessing.Process(target=sequential, args=(outputFile,1,9, )) # call functions that will find the solutions
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = perf_counter()

    print("Time taken: {}".format(end-start))
if __name__ == "__main__":
    main()
