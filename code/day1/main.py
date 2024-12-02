with open("input.txt", "r") as file:
    data = file.read()

l = [int(x) for x in data.replace("   ", "\n").split("\n")]
l1 = sorted(l[::2], reverse=True)
l2 = sorted(l[1::2], reverse=True)

res = 0
for x in range(len(l1)):
    res += abs(l1[x] - l2[x])
print(res)

res2 = 0
for x in range(len(l1)):
    res2 += l1[x] * l2.count(l1[x])

print(res2)