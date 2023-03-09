N, L = map(int, input().split())

current = time = 0

for _ in range(N):
    D, R, G = map(int, input().split())

    time += D - current
    current = D

    if time % (R + G) < R:
        time += (R - (time % (R + G)))

time += L - current
    
print(time)