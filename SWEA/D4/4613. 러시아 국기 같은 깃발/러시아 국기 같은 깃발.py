T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    min_value = 2501
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            value = 0
            for a in range(i + 1):
                for b in range(M):
                    if arr[a][b] != 'W':
                        value += 1

            for a in range(i + 1, j + 1):
                for b in range(M):
                    if arr[a][b] != 'B':
                        value += 1

            for a in range(j + 1, N):
                for b in range(M):
                    if arr[a][b] != 'R':
                        value += 1

            if min_value > value:
                min_value = value

    print(f'#{test_case} {min_value}')