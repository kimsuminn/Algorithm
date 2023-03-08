from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    X = input()[1:-1].split(',')

    que = deque(X)
    check = 0

    if n == 0:
        que = []

    for i in p:
        if i == 'R':
            check += 1

        elif i == 'D':
            if len(que) == 0:
                print('error')
                break
            else:
                if check % 2:
                    que.pop()
                else:
                    que.popleft()

    else:
        if check % 2 == 0:
            print(f'[{",".join(que)}]')
        else:
            que.reverse()
            print(f'[{",".join(que)}]')
