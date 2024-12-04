lines = [line.strip() for line in open("input.txt", "r").readlines()]

sum = 0
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        if lines[i][j] == 'A':
            if (lines[i - 1][j - 1] == 'M' and lines[i + 1][j + 1] == 'S' and lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S') or (lines[i - 1][j - 1] == 'M' and lines[i + 1][j + 1] == 'S' and lines[i - 1][j + 1] == 'S' and lines[i + 1][j - 1] == 'M') or (lines[i - 1][j - 1] == 'S' and lines[i + 1][j + 1] == 'M' and lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S') or (lines[i - 1][j - 1] == 'S' and lines[i + 1][j + 1] == 'M' and lines[i - 1][j + 1] == 'S' and lines[i + 1][j - 1] == 'M'): sum += 1
print(sum)
