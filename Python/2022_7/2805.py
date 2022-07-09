#2805 나무자르기 실버2 / python3로 시간초과떠서 pypy로 제출
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
tree=list(map(int,input().split()))
#4,7로 입력받아 20 15 10 17로 하면 나머지가 7이 남도록 해서 15의 길이가 나온다.
start,end=1,max(tree)
while start<=end:
    mid=(start+end)//2
    #print(m)
    last=0
    for i in tree:

        if i>=mid:
            last+=(i-mid)
    #print(last)
    if last>=m:
        start=mid+1
    else:
        end=mid-1
    #else:
        #break
print(end)
