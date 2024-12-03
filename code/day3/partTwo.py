x = __import__('re').findall("(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", open("input.txt", "r").read())

enabled = True

sum = 0
for exp in x:
    if exp[1]:
        enabled = True
    elif exp[2]:
        enabled = False
    else:
        if enabled:
            params = [int(x) for x in exp[0][4:-1].split(",")]
            sum += (params[0] * params[1])
print(sum)