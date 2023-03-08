N = int(input())

arr = [[0] * 1002 for _ in range(1002)]
for n in range(1, N + 1):
    x, y, w, h = map(int, input().split())

    for i in range(x, x + w):
        for j in range(y, y + h):
            arr[i][j] = n

for i in range(1, N + 1):
    cnt = 0
    for j in range(1002):
        for k in range(1002):
            if arr[j][k] == i:
                cnt += 1

    print(cnt)