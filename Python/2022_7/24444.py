#실버2 24444 알고리즘 수업 - 너비 우선 탐색 1 
#처음 공부하는 개념으로 코드를 참고하였습니다.

import sys
input=sys.stdin.readline
from collections import deque

n,m,r=map(int,input().split())
line=[[] for _ in range(n+1)] #여기서 라인은 단계라고 생각하면 됨. 앞에서부터 차례차례 진행을 하게됨.

for i in range(m):
    u,v=map(int,input().split())
    line[u].append(v)
    line[v].append(u)
    
for i in range(n+1):
    line[i].sort()

def bfs(line, r,visited):
    queue=deque([r]) #FIFO를 위해 deque로 만들어주고
    visited[r]=1 #시작점에 대해서는 당연히 첫번째
    cnt=2 #그 이후에 대해서는 카운트 대비

    while queue:
        r=queue.popleft() #순서가 다시 되게 되면 뽑아주는데
        for i in line[r]:
            if visited[i]==0: #처음 접근하는 거라면
                queue.append(i) #일단 접근해서 i를 queue에 추가해주고
                visited[i]=cnt #그리고 접근했으니까 그 순서를 기록해서
                cnt+=1 #순서 다음것을 위해 올려준다.
visited=[0]*(n+1) #기록 순서를 위해 리스트를 미리 만들고
bfs(line,r,visited) #이건 함수 호출

for i in visited[1::]:
    print(i)
