#heute gar keine zeit für minmaxing..
lines = [line.strip() for line in open("input.txt", "r").readlines()]

sum = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'X':
            if j + 3 < len(lines[i]) and lines[i][j + 1] == 'M' and lines[i][j + 2] == 'A' and lines[i][j + 3] == 'S':
                sum += 1
            if j - 3 >= 0 and lines[i][j - 1] == 'M' and lines[i][j - 2] == 'A' and lines[i][j - 3] == 'S':
                sum += 1
            if i + 3 < len(lines) and lines[i + 1][j] == 'M' and lines[i + 2][j] == 'A' and lines[i + 3][j] == 'S':
                sum += 1
            if i - 3 >= 0 and lines[i - 1][j] == 'M' and lines[i - 2][j] == 'A' and lines[i - 3][j] == 'S':
                sum += 1
            if i + 3 < len(lines) and j + 3 < len(lines[i]) and \
               lines[i + 1][j + 1] == 'M' and lines[i + 2][j + 2] == 'A' and lines[i + 3][j + 3] == 'S':
                sum += 1
            if i - 3 >= 0 and j - 3 >= 0 and \
               lines[i - 1][j - 1] == 'M' and lines[i - 2][j - 2] == 'A' and lines[i - 3][j - 3] == 'S':
                sum += 1
            if i + 3 < len(lines) and j - 3 >= 0 and \
               lines[i + 1][j - 1] == 'M' and lines[i + 2][j - 2] == 'A' and lines[i + 3][j - 3] == 'S':
                sum += 1
            if i - 3 >= 0 and j + 3 < len(lines[i]) and \
               lines[i - 1][j + 1] == 'M' and lines[i - 2][j + 2] == 'A' and lines[i - 3][j + 3] == 'S':
                sum += 1

print(sum)
