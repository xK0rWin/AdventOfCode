print(sum(exp[0] * exp[1] for exp in [[int(x) for x in line[4:-1].split(",")] for line in __import__('re').findall("mul\(\d{1,3},\d{1,3}\)", open("input.txt", "r").read())]))