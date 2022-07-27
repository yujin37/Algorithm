#실버2 24479 알고리즘 수업 - 깊이 우선 탐색 1
#익히는 차원에서 코드 보고 학습함
import sys
sys.setrecursionlimit(10**9) #제한이 필요하다고 해서
input = sys.stdin.readline #빠른 입츨력

N,M,R=map(int,input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

for i in range(M):
    u,v=map(int,input().split()) #입력받고
    graph[u].append(v) #위치에 넣어주는데
    graph[v].append(u)
#print(graph)

def dfs(x):
    global count #함수 내에서 변수를 그대로 사용하려고
    visited[x]=count #방문 기록에 변수위치에 count값 넣고
    graph[x].sort() #정렬? 근데 왜 해야 하는지를 모름

    for i in graph[x]:
        if visited[i]==0: #한번도 카운트 안되었다면
            count+=1 #카운트 해주고
            dfs(i) #다시 불러와서 위에 visited와 graph 정렬을 해준다.
 
dfs(R) #함수 호출

for i in range(1,N+1):
    print(visited[i])
