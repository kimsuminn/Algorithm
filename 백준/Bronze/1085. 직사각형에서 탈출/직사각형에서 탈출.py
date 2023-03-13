x, y, w, h = map(int, input().split())

mn = 1000
if mn > x:
    mn = x

if mn > y:
    mn = y

if mn > w - x:
    mn = w - x

if mn > h - y:
    mn = h - y

print(mn)