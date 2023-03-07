T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1): 
            num = 0
            for k in range(M):
                for l in range(M):
                    if j + k > N - 1:
                        continue

                    num += arr[i + k][j + l]
            
            if mx < num:
                mx = num
            
    print(f'#{test_case} {mx}')