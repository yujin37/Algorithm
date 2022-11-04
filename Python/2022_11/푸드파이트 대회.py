def solution(food):
    answer = ''
    cnt=[]
    rep=0
    for i in range(len(food)):
        cnt.append(food[i]//2)
        rep+=(food[i]//2)
    i=0
    while i<len(food):
        if cnt[i]==0:
            i+=1
        else:
            for j in range(cnt[i]):
                answer+=str(i)
                cnt[i]-=1
    answer=answer+'0'+answer[::-1]
    return answer
