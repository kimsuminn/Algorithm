H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]

result = [[-1] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            result[i][j] = 0
            for k in range(j + 1, W):
                result[i][k] = k - j

for i in range(H):
    print(*result[i])
