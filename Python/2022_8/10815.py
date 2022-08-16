#실버5 숫자카드
import sys
input=sys.stdin.readline
n=int(input())
card=list(map(int,input().split()))
m=int(input())
card2=list(map(int,input().split()))
card.sort()
#이분탐색 시작
def search(target,line, st, ed):
    if st>ed:
        return 0
    mid=(st+ed)//2
    if line[mid]>target:
        ed=mid-1
        return search(target,line,st,ed)
    elif line[mid]<target:
        st=mid+1
        return search(target,line,st,ed)
    else:
        return 1
    return 0

num_card=[]
for i in card2:
    start=0
    end=n-1
    re=search(i,card, start,end)
    num_card.append(re)
for i in range(m):
    print(num_card[i],end=" ")
