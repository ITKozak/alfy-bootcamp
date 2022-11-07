#! /usr/bin/python

# TODO: comment all this bits.

def input_list() -> list:
    user_input = list()
    while True:
        user_input.append(input())
        if user_input[-1] == '' or user_input[-1] == ' ':
            user_input[-1] = 0
            break
    for i in range(len(user_input) - 1):
        user_input[-1] += float(user_input[i])
    return user_input

def check_monotonic_sequence(sequence: list) -> list:
    copy_list = sequence.copy()
    copy_list.sort()
    check = [False] * 4
    if copy_list == sequence:
        check[0], check[1] = True, True
        for i in range(1, len(copy_list)):
            if copy_list[i-1] == copy_list[i]:
                check[1] = False
                break
    copy_list.reverse()
    if copy_list == sequence:
        check[2], check[3] = True, True
        for i in range(1, len(copy_list)):
            if copy_list[i-1] == copy_list[i]:
                check[3] = False
                break
    return check

def check_monotonic_sequence_inverse(sequence: list) -> list:
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
    prime_list = list()
    current_iterator = 2
    while len(prime_list) < n:
        for e in range(2, current_iterator):
            if (current_iterator % e) == 0:
                current_iterator += 1
                break
        else:
            prime_list.append(current_iterator)
            current_iterator += 1
    return prime_list

def calc_the_inner_product(vec_1: list, vec_2: list) -> int:
    if len(vec_1) != len(vec_2):
        return None
    inner_product = 0
    for e in range(len(vec_1)):
        inner_product += vec_1[e] * vec_2[e]
    return inner_product

def vectors_list_sum(vec_lst: list) -> list:
    vec_sum = [0] * len(vec_lst[0])
    for e in vec_lst:
        for i in range(len(e)):
            vec_sum[i] += e[i]
    return vec_sum

def orthogonal_number(vectors: list) -> float:
    ort_num = 0
    for e in range(len(vectors)):
        for i in range(e + 1, len(vectors)):
            if calc_the_inner_product(vectors[e], vectors[i]) == 0:
                ort_num += 1
    return ort_num