#실버2, 도영이가 만든 맛있는 음식
import sys
from itertools import combinations
input=sys.stdin.readline
n=int(input())
taste=[]
ans=1000000000

for i in range(1,n+1):
    t1,t2=input().split()
    t1=int(t1)
    t2=int(t2)
    taste.append([t1,t2])

test=list(combinations(taste,i) for i in range(1,n+1)) #이걸로 조합을 만든다. 경우의 수임.

for i in test:
    
    for j in i:
        S,B=1,0
        
        for E in j:
            S*=E[0]
            B+=E[1]
        
        ans=min(ans, abs(B-S))
        
        
   
print(ans)

