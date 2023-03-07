T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    min_Value = 1000
    for i in range(N - 2):
        for j in range(i + 1, N - 1):

            if arr[i] != arr[i + 1] and arr[j] != arr[j + 1]:
                A = i + 1
                B = j - i
                C = N - 1 - j

                if A * B * C != 0 and A <= N // 2 and B <= N // 2 and C <= N // 2:
                    n = max(A, B, C) - min(A, B, C)
                    if min_Value > n:
                        min_Value = n

    if min_Value == 1000:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {min_Value}')