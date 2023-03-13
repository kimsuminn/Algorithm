N = int(input())

arr = [0] * 1001
mx_i = mx = 0
for _ in range(N):
    L, H = map(int, input().split())

    arr[L] = H

    if mx < H:
        mx_i, mx = L, H

ans = mx = 0
for i in range(mx_i + 1):
    mx = max(mx, arr[i])
    ans += mx

mx = 0
for i in range(1000, mx_i, -1):
    mx = max(mx, arr[i])
    ans += mx

print(ans)