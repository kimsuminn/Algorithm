def solution(my_string):
    answer = ''
    for i in my_string:
        answer += i.lower()
        
    answer = list(answer)
    answer.sort()
    answer = ''.join(answer)
    return answer