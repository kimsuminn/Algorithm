N, K = map(int, input().split())
arr = list(map(int, input().split()))

part = sum(arr[:K])
sum_list = [part]

for i in range(N - K):
    part = part - arr[i] + arr[i + K]
    sum_list.append(part)

print(max(sum_list))