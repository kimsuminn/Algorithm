for test_case in range(1, 11):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for i in range(100):
        check = False
        for j in range(100):
            if lst[j][i] == 1:
                check = True
            elif lst[j][i] == 2:
                if check:
                    result += 1
                    check = False

    print(f'#{test_case} {result}')