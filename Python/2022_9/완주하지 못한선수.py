#일반 솔루션
def solution(participant, completion):
    p2=participant
    #print(p2)
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
    return participant[-1]
#해시 솔루션
def solution(participant, completion):
    test={}
    temp=0
    for i in participant:
        test[hash(i)]=i
        temp+=int(hash(i))
    for j in completion:
        temp-=int(hash(j))
    answer=test[temp]
    return answer
