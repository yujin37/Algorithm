#11279 최대 힙, 실버2
import sys
import heapq
input=sys.stdin.readline

n=int(input())
program=[]
for i in range(n):
    x=int(input())
    if x==0:
        if len(program)==0:
            print(0)
        else:
            print(heapq.heappop(program)[1])
    elif x>0:
        heapq.heappush(program,(-x,x))
