T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    di_1 = [-1, 0, 1, 0]
    dj_1 = [0, 1, 0, -1]

    di_2 = [-1, 1, 1, -1]
    dj_2 = [-1, 1, -1, 1]

    mx = 0

    for i in range(N):
        for j in range(N):
            total_1 = lst[i][j]
            total_2 = lst[i][j]
            for l in range(1, M):
                for k in range(4):
                    ni_1 = i + di_1[k] * l
                    nj_1 = j + dj_1[k] * l

                    ni_2 = i + di_2[k] * l
                    nj_2 = j + dj_2[k] * l

                    if 0 <= ni_1 < N and 0 <= nj_1 < N:
                        total_1 += lst[ni_1][nj_1]

                    if 0 <= ni_2 < N and 0 <= nj_2 < N:
                        total_2 += lst[ni_2][nj_2]

            if mx < total_1:
                mx = total_1

            if mx < total_2:
                mx = total_2

    print(f'#{test_case} {mx}')
