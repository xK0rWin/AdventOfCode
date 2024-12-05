parts = open("input.txt", "r").read().split("\n\n")
updates = [list(map(int, update.split(",")))[::-1] for update in parts[1].split("\n")]
rules_dict = __import__('collections').defaultdict(list)
for key, value in [tuple(map(int, x.split("|"))) for x in parts[0].split("\n")]:
    rules_dict[key].append(value)

print(sum(update[int(len(update) / 2)] for update in updates if not any(other in update[i + 1:] for i, item in enumerate(update) for other in rules_dict[item])))