last = [1]
print(sum(val for val in list(map(lambda val: last.__setitem__(0, int(val)) or last[0] if val.isdigit() else eval(val) * last[0], [__import__('re').sub(r"mul\((\d+),(\d+)\)", r"\1 * \2", __import__('re').sub(r"do\(\)", "1", __import__('re').sub(r"don't\(\)", "0", item)) if __import__('re').search(r"do\(\)", item) or __import__('re').search(r"don't\(\)", item) else item) for item in __import__('re').findall("(?:mul\(\d{1,3},\d{1,3}\))|(?:do\(\))|(?:don't\(\))", open("input.txt", "r").read())])) if val != 1))

