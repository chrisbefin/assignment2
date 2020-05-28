import random
from time import perf_counter

def pemdas():
    time_start = perf_counter()
    options = [1,2,3,4,5,6,7,8,9]
    starting_numbers = [1,2,3,4,5,6,7,8,9]
    solutions = 0
    total_checks = 0
    for x2 in starting_numbers:
        options = [1,2,3,4,5,6,7,8,9]
        options.remove(x2)
        x3_options = options.copy()
        for x3 in x3_options:
            x7_options = x3_options.copy()
            x7_options.remove(x3)
            for x7 in x7_options:
                x8_options = x7_options.copy()
                x8_options.remove(x7)
                for x8 in x8_options:
                    x9_options = x8_options.copy()
                    x9_options.remove(x8)
                    for x9 in x9_options:
                        x6_options = x9_options.copy()
                        x6_options.remove(x9)
                        for x6 in x6_options:
                            x1_options = x6_options.copy()
                            x1_options.remove(x6)
                            for x1 in x1_options:
                                x4_options = x1_options.copy()
                                x4_options.remove(x1)
                                for x4 in x4_options:
                                    x5_options = x4_options.copy()
                                    x5_options.remove(x4)
                                    for x5 in x5_options:
                                        total_checks += 1
                                        if (x1+13*x2/x3+x4+12*x5-x6-11+x7*x8/x9-10 == 66.0000):
                                            solutions += 1

    time_end = perf_counter()
    print("{} checks performed and {} PEMDAS solutions found in {} seconds".format(total_checks, solutions, time_end-time_start))


def sequential():
    time_start = perf_counter()
    options = [1,2,3,4,5,6,7,8,9]
    starting_numbers = [1,2,3,4,5,6,7,8,9]
    solutions = 0
    total_checks = 0
    for x2 in starting_numbers:
        options = [1,2,3,4,5,6,7,8,9]
        options.remove(x2)
        x3_options = options.copy()
        for x3 in x3_options:
            x7_options = x3_options.copy()
            x7_options.remove(x3)
            for x7 in x7_options:
                x8_options = x7_options.copy()
                x8_options.remove(x7)
                for x8 in x8_options:
                    x9_options = x8_options.copy()
                    x9_options.remove(x8)
                    for x9 in x9_options:
                        x6_options = x9_options.copy()
                        x6_options.remove(x9)
                        for x6 in x6_options:
                            x1_options = x6_options.copy()
                            x1_options.remove(x6)
                            for x1 in x1_options:
                                x4_options = x1_options.copy()
                                x4_options.remove(x1)
                                for x4 in x4_options:
                                    x5_options = x4_options.copy()
                                    x5_options.remove(x4)
                                    for x5 in x5_options:
                                        total_checks += 1
                                        if (x1+13*x2/x3+x4+12*x5-x6-11+x7*x8/x9-10 == 66.0000):
                                            solutions += 1

    time_end = perf_counter()
    print("{} checks performed and {} sequential solutions found in {} seconds".format(total_checks, solutions, time_end-time_start))
if __name__ == "__main__":
    pemdas()
    sequential()
