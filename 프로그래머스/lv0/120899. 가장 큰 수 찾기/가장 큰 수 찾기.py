def solution(array):
    mx, idx = 0, 0
    for i, value in enumerate(array):
        if mx < value:
            mx = value
            idx = i
    answer = [mx, idx]
    return answer