def is_safe(l):
    return (l == sorted(l) or l == sorted(l, reverse=True)) and all(1 <= abs(l[i] - l[i + 1]) <= 3 for i in range(len(l) - 1))

def safe_with_damp(l):
    for x in range (len(l)):
        modififedList = l.copy()
        modififedList.pop(x)
        if is_safe(modififedList): return True
    return False

with open("input.txt", "r") as file:
    print(sum(1 for l in [[int(x) for x in line.split()] for line in file] if (l == sorted(l) or l == sorted(l, reverse=True)) and all(1 <= abs(l[i] - l[i + 1]) <= 3 for i in range(len(l) - 1)) or safe_with_damp(l)))