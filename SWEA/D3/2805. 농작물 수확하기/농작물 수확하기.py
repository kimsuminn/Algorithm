T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]

    center = N // 2
    result = 0

    for i in range(N):
        for j in range(N):
            if abs(center - i) + abs(center - j) <= N // 2:
                result += lst[i][j]

    print(f'#{test_case} {result}')
