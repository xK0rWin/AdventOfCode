from collections import defaultdict
parts = open("input.txt", "r").read().split("\n\n")

updates = [list(map(int, update.split(",")))[::-1] for update in parts[1].split("\n")]
rules =[tuple(map(int, x.split("|"))) for x in parts[0].split("\n")]

rules_dict = defaultdict(list)
for key, value in rules:
    rules_dict[key].append(value)

sum = 0
for update in updates:
    if not any(other in update[i + 1:] for i, item in enumerate(update) for other in rules_dict[item]):
        sum += update[int(len(update) / 2)]

print(sum)