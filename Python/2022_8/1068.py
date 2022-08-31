#골드5 트리
import sys
input=sys.stdin.readline

n=int(input())

result=[[] for _ in range(n)]
node=list(map(int,input().split()))
#print(result)
x=int(input())
for i in range(n):
    result[i]=node[i]

def delete(x):
    result[x]=-2
    for i in range(n):
        if result[i]==x:
            result[i]=-2
            delete(i)

delete(x)
cnt=0

for i in range(n):
    if result[i]!=-2:
        err=0
        for j in result:
            if j==i:
                err=1
        if err==0:
            cnt +=1
print(cnt)
