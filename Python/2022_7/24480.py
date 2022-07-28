#실버2 24480 알고리즘 수업 - 깊이 우선 탐색 2
#앞 문제에서 정렬만 반대로 해줌

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N,M,R=map(int,input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

for i in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
#print(graph)

def dfs(x):
    global count
    visited[x]=count
    graph[x].sort(reverse=True)

    for i in graph[x]:
        if visited[i]==0:
            count+=1
            dfs(i)

dfs(R)

for i in range(1,N+1):
    print(visited[i])
