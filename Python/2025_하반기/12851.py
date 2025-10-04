import sys
from collections import deque

input = sys.stdin.readline

def split_case(num):
    plus = num + 1
    minus = num - 1
    multi = num * 2
    return [plus, minus, multi]
n, k = map(int,input().split())
def bfs(subin):
    
    queue = deque()
    queue.append(subin)
    visited = [-1] * 100001
    visited[subin] = 0
    cnt = 0
    while queue:
        now = queue.popleft()
        if now == k:
            cnt += 1
        for check in split_case(now):
            if 0<= check <= 100000:
                if visited[check] == -1 or visited[check] >= visited[now] + 1:
                    visited[check] = visited[now] + 1
                    queue.append(check)
            
    return visited[k], cnt

result_time, result_cnt = bfs(n) #가장 짧은 시간
print(result_time)
print(result_cnt)
#print(graph)