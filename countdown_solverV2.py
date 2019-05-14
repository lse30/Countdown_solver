def dfs_backtrack(candidate, input, output):
    if is_solution(candidate, len(input)):
        add_to_output(candidate, output)
    else:
        for child_candidate in children(candidate, input):
            if not should_prune(child_candidate):
                dfs_backtrack(child_candidate, input, output)

def is_solution(candidate, desired_length):
    return len(candidate) == desired_length

def children(candidate, input):
    if candidate == []:
        output = [[a] for a in input]
        return output
    else:
        list_input = list(input)
        output = []
        for item in list_input:
            temp = candidate
            temp = temp + [item]
            output.append(temp)

        return output

def add_to_output(candidate, output):
    output.append(tuple(candidate))

def should_prune(candidate):
    if len(candidate) == 1:
        return False
    else:
        value_set = set()
        for value in candidate:
            value_set.add(value)
        return len(candidate) != len(value_set)

def permutations(s):
    solutions = []
    dfs_backtrack([], s, solutions)
    return solutions

print(len(permutations([100, 9, 10, 2, 6, 1])))

