T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()

    num = 0
    result = 'Possible'
    for i in range(N):
        num += 1
        cnt = (time[i] // M) * K
        if cnt - num < 0:
            result = 'Impossible'
            break

    print(f'#{test_case} {result}')
