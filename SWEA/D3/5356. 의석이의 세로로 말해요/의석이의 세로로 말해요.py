T = int(input())
for test_case in range(1, T + 1):
    text = [list(input()) for _ in range(5)]

    i = 0
    result = ''
    while True:
        if text[0] == [] and text[1] == [] and text[2] == [] and text[3] == [] and text[4] == []:
            break

        if i >= 5:
            i = 0

        if len(text[i]) >= 1:
            result += text[i][0]
            text[i].pop(0)

        i += 1

    print(f'#{test_case} {result}')