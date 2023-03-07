T = int(input())

for test_case in range(1, T + 1):
    w = int(input())
    box = list(map(int, input().split()))

    result = []
    for i in range(w):
        cnt = 0
        for j in range(i, w):
            if box[i] > box[j]:
                cnt += 1
        result.append(cnt)

    print(f'#{test_case} {max(result)}')