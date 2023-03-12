N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
while True:
    if not A and not B:
        break

    result += max(B) * min(A)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(result)