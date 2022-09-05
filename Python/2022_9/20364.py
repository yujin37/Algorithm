#실버2 부동산다툼
import sys
input=sys.stdin.readline

n,q=map(int,input().split())
find=[int(input()) for _ in range(q)]

visit=set()

for i in range(q):
    result=0
    f=find[i]
    while f>1:
        if f in visit:
            result=f
        f//=2
    visit.add(find[i])
    print(result)
