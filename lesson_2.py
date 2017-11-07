m, n = [int(i) for i in input().split(' ')]
arr = [[int(j) for j in input().split(' ')[:n]] for i in range(m)]
i, j = [int(i) for i in input().split(' ')]
for row in arr:
    row[i], row[j] = row[j], row[i]
for row in arr:
    print(*row)
