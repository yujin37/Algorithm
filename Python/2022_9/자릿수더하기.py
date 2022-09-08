def solution(n):
    answer = 0
    
    nn=list(str(n))
    for i in range(len(nn)):
        answer+=int(nn[i])

    return answer
