n = int(input())

arr = [[0] * 102 for _ in range(102)]
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x + 1, x + 11):
        for j in range(y + 1, y + 11):
            arr[i][j] = 1

result = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 0 and arr[i][j + 1] == 1:
            result += 1

        if arr[i][j] == 1 and arr[i][j + 1] == 0:
            result += 1

        if arr[i][j] == 0 and arr[i + 1][j] == 1:
            result += 1

        if arr[i][j] == 1 and arr[i + 1][j] == 0:
            result += 1

print(result)
