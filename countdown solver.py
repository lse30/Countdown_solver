import time

def solver(numbers, target):
    start_time = time.time()
    num_orders = []
    used_nums = []

    for first in range(0,6):

        used_nums.append(first)

        for second in range(0,6):

            if second not in used_nums:
                used_nums.append(second)

                for third in range(0,6):

                    if third not in used_nums:
                        used_nums.append(third)

                        for forth in range(0,6):

                            if forth not in used_nums:
                                used_nums.append(forth)

                                for fifth in range(0,6):

                                    if fifth not in used_nums:
                                        used_nums.append(fifth)

                                        for sixth in range(0,6):

                                            if sixth not in used_nums:
                                                nums = [numbers[first],
                                                        numbers[second],
                                                        numbers[third],
                                                        numbers[forth],
                                                        numbers[fifth],
                                                        numbers[sixth],]
                                                num_orders.append(nums)

                                        used_nums.remove(fifth)
                                used_nums.remove(forth)
                        used_nums.remove(third)
                used_nums.remove(second)
        used_nums.remove(first)


    operators = ['a','s','m','d']
    op_sequence = []

    for operator_1 in operators:
        for operator_2 in operators:
            for operator_3 in operators:
                for operator_4 in operators:
                    for operator_5 in operators:
                        op_list = [operator_1, operator_2, operator_3, operator_4, operator_5]
                        op_sequence.append(op_list)


    for num_order in num_orders:
        for sequence in op_sequence:

            i = 0
            while i <= 5:

                if i == 0:
                    current = num_order[0]
                else:
                    if sequence[i-1] == 'a':
                        current += num_order[i]
                    elif sequence[i-1] == 's':
                        current -= num_order[i]
                    elif sequence[i-1] == 'm':
                        current *= num_order[i]
                    else:
                        current /= num_order[i]
                if current == target:
                    start = str(target) + ' = ' + str(num_order[0])
                    j = 0
                    while j < i:
                        if sequence[j] == 'a':
                            use = '+'
                        elif sequence[j] == 's':
                            use = '-'
                        elif sequence[j] == 'm':
                            use = '*'
                        else:
                            use = '/'
                        string = use + ' ' + str(num_order[j+1])
                        start += ' ' + string
                        j += 1
                    time_elapsed = time.time()
                    print('time taken: ', (time_elapsed-start_time))

                    return start


                i += 1


"""This is the first attempt at making code that can generate every possible way of adding, subtracting
multiplying and dividing numbers in attempt to find the target number
it does not work for all numbers because this version does not try every possible combination
for example the list [1, 6, 2, 10, 25, 100] and target 863 will return None however the solution is 
863 = (10-1)*100-25-(2*6)
this is impossible to create without using brackets and therefore cannot be made in the solver
"""

"""To use"""
"""change the target variable to your target and set the number_list variable to
 your list of the 6 numbers that are given
NOTE the show allows for duplicate numbers and so does the solver
an example is shown below
target = 864
number_list = [1, 6, 2, 10, 25, 100]
"""

target = 864
number_list = [1, 6, 2, 10, 25, 100]

answer = solver(number_list, target)
print(answer)

"""the number is printed followed by the order of operations"""
"""DO NOT APPLY BEDMAS, 
    Simply read the inputs from left to right:
    EXAMPLE: 864 = 2 * 10 - 1 + 25 + 100 * 6
    implies:
    2 * 10 = 20
    20 - 1 = 19
    19 + 25 = 44
    44 + 100 = 144
    144 * 6 = 864"""


