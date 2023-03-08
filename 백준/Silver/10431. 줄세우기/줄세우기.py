T = int(input())

for _ in range(T):
    test_case, *lst = map(int, input().split())

    cnt = 0
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] < lst[j]:
                cnt += 1
    print(test_case, cnt)
