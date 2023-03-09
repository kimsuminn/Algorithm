bingo_lst = [list(map(int, input().split())) for _ in range(5)]

answer = []
for _ in range(5):
    answer += list(map(int, input().split()))

check = [0] * 12
bingo = num = 0

for n in range(25):
    num = n

    if bingo >= 3:
        break
    
    for i in range(5):
        if bingo >= 3:
            break

        for j in range(5):
            if bingo >= 3:
                break

            if bingo_lst[i][j] == answer[n]:
                bingo_lst[i][j] = 0
                check[i] += 1
                check[j + 5] += 1

                if i == j:
                    check[10] += 1

                if i + j == 4:
                    check[11] += 1

                for k in range(12):
                    if check[k] == 5:
                        check[k] = 0
                        bingo += 1

                    if bingo >= 3:
                        break

print(num)