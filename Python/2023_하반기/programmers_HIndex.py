def solution(citations):
    answer = 0
    for h in range(1,len(citations)+1):
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= h:
                cnt += 1
        if cnt >= h and len(citations)-cnt <= h:
            answer = h
        
    return answer
print(solution([3,0,6,1,5]))