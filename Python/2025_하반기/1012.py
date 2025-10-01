import sys
from collections import deque
input = sys.stdin.readline

def bfs(soil, start_h, start_w):
    queue = deque([[start_h, start_w]])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    soil[start_h][start_w] = 0
    while queue:
        target = queue.popleft()
        
        target_h, target_w = target[0], target[1]
        for s in range(4):
            if 0<=target_h +dx[s] < m and 0<=target_w+dy[s] < n:
                if soil[target_h+dx[s]][target_w+dy[s]] == 1:
                    queue.append([target_h+dx[s],target_w+dy[s]])
                    soil[target_h+dx[s]][target_w+dy[s]] = 0
    
        
t = int(input())
for i in range(t):
    m, n, k = map(int,input().split())
    worm = 0 #지렁이 개수 
    ground = [[0 for _ in range(n)] for _ in range(m)]
    
    for j in range(k):
        x, y = map(int,input().split())
        ground[x][y] = 1
        
    for o in range(m):
        for p in range(n):
            if ground[o][p] == 1:
                bfs(ground, o, p)
                worm += 1
    
    print(worm)