import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
stack=[]
ans=[-1 for _ in range(n)]

for i in range(n):

    while stack and a[stack[-1]]<a[i]:
        ans[stack.pop()]=a[i]
    stack.append(i)
print(*ans)