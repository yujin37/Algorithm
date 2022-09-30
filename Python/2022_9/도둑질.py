#프로그래머스, DP문제
def solution(money):
    answer = 0
    r1=[0]*len(money)

    
    r1[0]=money[0]
    r1[1]=max(money[0], money[1])

    for i in range(2,len(money)-1):
        r1[i]=max(r1[i-2]+money[i], r1[i-1])

    r2=[0]*len(money)

    r2[1]=money[1]

    for i in range(2,len(money)):
        r2[i]=max(r2[i-2]+money[i], r2[i-1])
    answer=max(max(r1), max(r2))
        
    #print(r1,r2)       
        
    return answer
