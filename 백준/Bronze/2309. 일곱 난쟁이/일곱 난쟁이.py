height = [int(input()) for _ in range(9)]
height.sort()

hap = sum(height)
idx = []

for i in range(8):
    for j in range(i + 1, 9):
        result = hap - height[i] - height[j]
        if result == 100:
            break
    if result == 100:
        idx = [i, j]
        break

for i in range(9):
    if i in idx:
        continue
    else:
        print(height[i])