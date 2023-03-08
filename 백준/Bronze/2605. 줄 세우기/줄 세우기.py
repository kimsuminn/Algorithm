N = int(input())
lst = list(map(int, input().split()))
result = []

for i in range(N):
    result.insert(i - lst[i], i + 1)

print(*result)