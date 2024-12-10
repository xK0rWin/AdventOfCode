from itertools import product
def brute_force(result, numbers):
    for operators in product('+*', repeat=len(numbers) - 1):
        expression = f"({numbers[0]}{operators[0]}{numbers[1]})"
        for i in range(1, len(operators)):
            expression = f"({expression}{operators[i]}{numbers[i + 1]})"
        if (eval(expression) == result):
            return result
    return 0

print(sum(brute_force(int(eq[0]), list(map(int, eq[1].split()))) for eq in [e.split(":") for e in open("input.txt", "r").readlines()]))

