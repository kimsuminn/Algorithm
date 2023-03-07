T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_Value = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(1, arr[i][j] + 1):
                for l in range(4):
                    ni = i + di[l] * k
                    nj = j + dj[l] * k

                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]

            if max_Value < cnt:
                max_Value = cnt

    print(f'#{test_case} {max_Value}')