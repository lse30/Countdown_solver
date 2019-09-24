"""The third attempt at making a solver
This time im going to use recursion and start with a list of numbers and remove a number at each depth"""
import copy
import time


def dfs_backtrack(numbers, target, solutions):
    if is_solution(numbers[0], target):
        add_to_output(numbers[1], solutions)
    else:
        for child_candidate in children(numbers):
            dfs_backtrack(child_candidate, target, solutions)



def is_solution(candidate, target):
    return target in candidate


def children(numbers):
    output = []
    for i in range(len(numbers[0])):
        for j in range(i+1, len(numbers[0])):
            next = copy.deepcopy(numbers[0])
            next.pop(j)
            next.pop(i)
            new_numbers = operations(numbers[0][i], numbers[0][j])
            for item in new_numbers:
                numbers_list = next + [item[0]]
                path = copy.deepcopy(numbers[1])
                path.append(item[1])
                output.append([numbers_list, path])
    return output



def operations(a, b):
    output = []

    add = [a+b, (a, '+', b)]
    output.append(add)
    if a > b:
        sub_1 = [a-b, (a, '-', b)]
        output.append(sub_1)
    if b > a:
        sub_2 = [b-a, (b, '-', a)]
        output.append(sub_2)
    mul = [a*b, (a, '*', b)]
    output.append(mul)
    if a % b == 0 and b not in  [0,1]:
        div_1 = [int(a/b), (a, '/', b)]
        output.append(div_1)
    if b % a == 0 and a not in [0,1]:
        div_2 = [int(b/a), (b, '/', a)]
        output.append(div_2)

    return output


def add_to_output(candidate, output):
    pretty_print(candidate)
    output.append(candidate)

def pretty_print(path):
    print("SOLUTION")
    for item in path:
        if item[1] == '+':
            string = str(item[0]) + ' ' + item[1] + ' ' + str(item[2]) + ' = ' + str(item[0] + item[2])
            print(string)
        if item[1] == '-':
            string = str(item[0]) + ' ' + item[1] + ' ' + str(item[2]) + ' = ' + str(item[0] - item[2])
            print(string)
        if item[1] == '*':
            string = str(item[0]) + ' ' + item[1] + ' ' + str(item[2]) + ' = ' + str(item[0] * item[2])
            print(string)
        if item[1] == '/':
            string = str(item[0]) + ' ' + item[1] + ' ' + str(item[2]) + ' = ' + str(int(item[0] / item[2]))
            print(string)
    print('\n')



def recursive_numbers_game_solver(numbers, target):
    start = time.time()
    solutions = []
    dfs_backtrack([numbers, []], target, solutions)
    if len(solutions) == 0:
        print("No Solutions!")
    else:
        print("There are", len(solutions), 'solutions.')
    print("Time Elapsed: {:.2f} seconds.".format((time.time() - start)))
    return


recursive_numbers_game_solver([3,4,4,10,25,50], 159)

