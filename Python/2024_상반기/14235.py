import heapq
n = int(input())
gift = []
for i in range(n):
    a = list(map(int,input().split()))
    if a[0] == 0: #거점지가 아닌 곳 
        if len(gift) == 0:
            print(-1)
        else:
            print(-1*heapq.heappop(gift))
    else: #거점지라면
        for j in range(1,len(a)):
            heapq.heappush(gift, -a[j])
