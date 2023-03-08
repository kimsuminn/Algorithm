w, h = map(int, input().split())

n = int(input())

cut_x = [0, w]
cut_y = [0, h]

for _ in range(n):
    d, num = map(int, input().split())

    if d == 0:
        cut_y.append(num)
    elif d == 1:
        cut_x.append(num)

cut_x.sort()
cut_y.sort()

x = []
y = []
for i in range(len(cut_x) - 1):
    x.append(cut_x[i + 1] - cut_x[i])

for i in range(len(cut_y) - 1):
    y.append(cut_y[i + 1] - cut_y[i])

print(max(x) * max(y))