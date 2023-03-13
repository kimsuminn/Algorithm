def solution(n):
    answer = 0
    while n != 0:
        temp = n % 10
        n //= 10
        answer += temp
    return answer