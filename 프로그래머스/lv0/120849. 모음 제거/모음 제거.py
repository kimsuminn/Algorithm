def solution(my_string):
    answer = ''
    for i in my_string:
        if i in 'aeiou':
            continue
        answer += i
    return answer