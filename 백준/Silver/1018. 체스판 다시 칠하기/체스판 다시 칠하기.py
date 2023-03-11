N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

mn_1 = mn_2 = 64

for x in range(N - 7):
    for y in range(M - 7):
        cnt_1 = cnt_2 = 0
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if arr[i][j] != 'W':
                            cnt_1 += 1
                        elif arr[i][j] != 'B':
                            cnt_2 += 1
                    elif j % 2 == 1:
                        if arr[i][j] != 'B':
                            cnt_1 += 1
                        elif arr[i][j] != 'W':
                            cnt_2 += 1
                else:
                    if j % 2 == 0:
                        if arr[i][j] != 'B':
                            cnt_1 += 1
                        elif arr[i][j] != 'W':
                            cnt_2 += 1
                    elif j % 2 == 1:
                        if arr[i][j] != 'W':
                            cnt_1 += 1
                        elif arr[i][j] != 'B':
                            cnt_2 += 1

        if mn_1 > cnt_1:
            mn_1 = cnt_1
            
        if mn_2 > cnt_2:
            mn_2 = cnt_2

print(min(mn_1, mn_2))