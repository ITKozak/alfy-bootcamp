#! /usr/bin/python

def calc_math_expression(num1, num2, operator):
    match operator:
        case "*":
            return num1 * num2
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case ":":
            if num2 == 0:
                return None
            return num1 / num2

def calc_math_expression_from_str(str_input):
    num1, operator, num2 = str_input.split()
    if operator in ["*", ":", "+", "-"]:
        return calc_math_expression(float(num1), float(num2), operator)
    else:
        return None

def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            return (num1, num3)
        else: 
            return (num1, num2)
    elif num3 >= num2 and num3 >= num1:
        if num2 >= num1:
            return (num3, num1)
        else:
            return (num3, num2)
    else:
        if num1 >= num3:
            return (num2, num3)
        return (num2, num1)    

def quadratic_equation_solver_from_user_input():
    a, b, c = input().split()
    if a == 0:
        return 1
    return quadratic_equation_solver(a, b, c)

def quadratic_equation_solver(a, b, c):
    if b*b < 4*a*c:
        return (None, None)
    disc = (b**2 - 4*a*c) ** 0.5
    solution_1 = (-b + disc) / (2*a)
    solution_2 = (-b - disc) / (2*a)
    if solution_1 == solution_2:
        solution_2 = None
    return (solution_1, solution_2)

def temp_checker(min_temp, temp_1, temp_2, temp_3):
    days = 0
    for temp in temp_1, temp_2, temp_3:
        if (temp > min_temp):
            days += 1
    if (days == 2):
        return True
    return False