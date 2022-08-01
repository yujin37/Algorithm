#실버3 11659 구간 합 구하기 4
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
num=list(map(int,input().split()))
sum_num=[0]
total=0
for i in range(N):
    total+=num[i]
    sum_num.append(total)
for i in range(M):
    s,e=map(int,input().split())
    print(sum_num[e]-sum_num[s-1])
