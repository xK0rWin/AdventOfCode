def is_safe(l):
    return (l == sorted(l) or l == sorted(l, reverse=True)) and all(1 <= abs(l[i] - l[i + 1]) <= 3 for i in range(len(l) - 1))

with open("input.txt", "r") as file:
    print(sum(1 for l in [[int(x) for x in line.split()] for line in file] if is_safe(l) or any(is_safe(l[:i] + l[i+1:]) for i in range(len(l)))))