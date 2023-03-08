N = int(input())

xy = [[0] * 100 for _ in range(101)]

arr = []
for i in range(N):
    x, y = map(int, input().split())
    x_1, y_1 = x, y
    x_2, y_2 = x + 10, y + 10
    for j in range(x_1, x_2):
        for k in range(y_1, y_2):
            xy[j][k] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if xy[i][j] > 0:
            cnt += 1

print(cnt)