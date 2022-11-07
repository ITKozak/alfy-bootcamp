#! /usr/bin/python


def input_list() -> list:
    '''Prompts user for input and return list with sum of input as a last item.
    '''
    user_input = list()
    while True:
        user_input.append(input())
        # Check if user finish entering array of numbers.
        if user_input[-1] == '' or user_input[-1] == ' ':
            user_input[-1] = 0
            break
    # Calculating sum of numbers in array.
    # len() - 1 used to prevent entering last elemnet.
    for i in range(len(user_input) - 1):
        user_input[-1] += float(user_input[i])
    return user_input

def check_monotonic_sequence(sequence: list) -> list:
    '''Check if provided sequence is a valid monotonic sequence.'''
    # Making copy of originall list for comparasions.
    copy_list = sequence.copy()
    copy_list.sort()
    check = [False] * 4
    # If sorted list equal to original - its monotonic up.
    if copy_list == sequence:
        check[0], check[1] = True, True
        # There we are checking if adjacent number is equal.
        # If they are - we have regular (non strong) monotonic.
        for i in range(1, len(copy_list)):
            if copy_list[i-1] == copy_list[i]:
                check[1] = False
                break
    # Doing previous part in revers to check down monotonic.
    # Also helps to check for absolut monotonic sequence, when
    # sequence could be up and down simultaneously.
    copy_list.reverse()
    if copy_list == sequence:
        check[2], check[3] = True, True
        for i in range(1, len(copy_list)):
            if copy_list[i-1] == copy_list[i]:
                check[3] = False
                break
    return check

def check_monotonic_sequence_inverse(sequence: list) -> list:
    '''Check if provided list of rules for monotonic sequence is possible.'''
    # Just using match with predefined matches.
    match sequence:
        case [True, True, True, True]:
            return [1]
        case [False, False, False, False]:
            return [1, -1, 1]
        case [True, True, False, False]:
            return [1, 2, 3]
        case [True, False, False, False]:
            return [1, 1, 2]
        case [False, False, True, False]:
            return [2, 1, 1]
        case [False, False, True, True]:
            return [3, 2, 1]
        case [True, False, True, False]:
            return [1, 1, 1]
        case _:
            return None

def primes_generator(n: int) -> list:
    '''Generate prime number list of given lenght'''
    prime_list = list()
    # First prime number is 2, so here we just skipping 1.
    current_iterator = 2
    # Run loop until we get list of required length.
    while len(prime_list) < n:
        # Once again, we starting from 2, because first prime number
        # and otherwise this will breake check.
        for e in range(2, current_iterator):
            # Checking if current number is not a prime by checking
            # reminder of division between current_iteratr and other 
            # numbers. If it dosent have a reminder - this isn't 
            # prime number.
            if (current_iterator % e) == 0:
                current_iterator += 1
                break
        # If number couldn't be devided without reminder - it's a prime
        # and we add this number to the list.
        else:
            prime_list.append(current_iterator)
            current_iterator += 1
    return prime_list

def calc_the_inner_product(vec_1: list, vec_2: list) -> int:
    '''Calculating inner product of two vectors'''
    # If number of elements in vectors are different - return None.
    if len(vec_1) != len(vec_2):
        return None
    inner_product = 0
    # Iterating through vectors elements and multiplying them.
    for e in range(len(vec_1)):
        inner_product += vec_1[e] * vec_2[e]
    return inner_product

def vectors_list_sum(vec_lst: list) -> list:
    '''Calculating sum of vectors'''
    # Defining returning vector with correct size
    vec_sum = [0] * len(vec_lst[0])
    # Iterrating through vectors and adding their element to the
    # returning vector.
    for e in vec_lst:
        for i in range(len(e)):
            vec_sum[i] += e[i]
    return vec_sum

def orthogonal_number(vectors: list) -> float:
    '''Calculating number of orthogonal vectors'''
    ort_num = 0
    # Itterating through len of vectors to get access to indexes.
    for e in range(len(vectors)):
        # e + 1 helps us to avoid checking vector with itself
        for i in range(e + 1, len(vectors)):
            # If sum of inner products of given vector 0 - they are 
            # orthogonal.
            if calc_the_inner_product(vectors[e], vectors[i]) == 0:
                ort_num += 1
    return ort_num