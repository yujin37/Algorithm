import heapq
n, m = map(int,input().split())
card = list(map(int,input().split()))
heapq.heapify(card)
for i in range(m):
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)
    tmp = n1 + n2
    heapq.heappush(card, tmp)
    heapq.heappush(card, tmp)
print(sum(card))