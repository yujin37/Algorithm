import sys
input=sys.stdin.readline
#약수 구하는 함수
def check(now):
    result=[]
    for i in range(1,int(now**(1/2))+1):
        if now % i == 0:
            result.append(i)
            if((i**2)!=now):
                result.append(now//i)
    result.sort()
    return result
#입력
n=int(input())
chk=list()
for i in range(n):
    num=int(input())
    chk.append(num)
#나머지를 없애기 위해 i-(i-1)로 처리
result=[]
for i in range(1,n):
    result.append(abs(chk[i]-chk[i-1]))
#약수 구해서 중복된 것 만 남기기
for i in range(n-1):
    if i==0:
        before=check(result[0])
        
    else:
        oopp=check(result[i])
        
        reco=[]
        for item in oopp:
            if item in before:
                reco.append(item)
        before=reco
    
for i in range(1,len(before)):
    print(before[i], end=' ')