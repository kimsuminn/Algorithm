# 롤 케이크의 길이 L
L = int(input())

# 방청객의 수
N = int(input())

mx_num = mx = 0 # 가장 많이 받을 것으로 기대한 방청객 번호와 기대된 조각 수
cake = [False] * (L + 1)
real_mx_num = real_mx = 0 # 실제로 많이 받는 방청객 번호와 조각 수

for i in range(N):
    Pi, Ki = map(int, input().split())
    sub = Ki - Pi + 1

    if mx < sub:
        mx = sub
        mx_num = i + 1

    cnt = 0
    for j in range(Pi, Ki + 1):
        if cake[j]:
            continue

        cake[j] = True
        cnt += 1

    if real_mx < cnt:
        real_mx = cnt
        real_mx_num = i + 1


print(mx_num)
print(real_mx_num)
