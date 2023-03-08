N, M = map(int, input().split())
card = list(map(int, input().split()))

total = 0
cnt = 99999999

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            num = card[i] + card[j] + card[k]
            if num <= M:
                if cnt > M - num:
                    cnt = M - num
                    total = num

print(total)