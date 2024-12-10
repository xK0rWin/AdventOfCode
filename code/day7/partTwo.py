from itertools import product
import re

def custom_evaluate(expression: str):
    elements = re.findall(r'\d+|[+*|]', expression)
    result = int(elements[0])
    for i in range(1, len(elements), 2):
        if elements[i] == "|":
            result = int(str(result) + str(elements[i + 1]))
        elif elements[i] == "+":
            result += int(elements[i + 1])
        else:
            result *= int(elements[i + 1])
    return result

def brute_force(result, numbers):
    for operators in product('+*|', repeat=len(numbers) - 1):
        expression = f"({numbers[0]}{operators[0]}{numbers[1]})"
        for i in range(1, len(operators)):
            expression = f"({expression}{operators[i]}{numbers[i + 1]})"
        if (custom_evaluate(expression) == result):
            return result
    return 0

print(sum(brute_force(int(eq[0]), list(map(int, eq[1].split()))) for eq in [e.split(":") for e in open("input.txt", "r").readlines()]))

