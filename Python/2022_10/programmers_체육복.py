def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    find=[]
    #2개 가지고 있는데 1개 도난당한 경우 처리
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]==reserve[j]:
                find.append(lost[i])
    #일부만 도난당한 경우 삭제
    for i in range(len(find)):
        reserve.remove(find[i])
        lost.remove(find[i])
    #나머지 나눠주는 경우
    for i in range(1,n+1):
        if i in lost:
            if i-1 in reserve:
                reserve.remove(i-1)
                answer+=1
            elif i+1 in reserve:
                reserve.remove(i+1)
                answer+=1

        else:
            answer+=1

    return answer
