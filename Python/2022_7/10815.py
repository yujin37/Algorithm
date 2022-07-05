import sys
n1=int(input())
num1=sorted(map(int,sys.stdin.readline().split()))
n2=int(input())
num2=list(map(int,sys.stdin.readline().split()))

def game(i,num1,start,end):
    if start>end:
        return 0
    m=(start+end)//2
    if i==num1[m]:
        return 1
    elif i<num1[m]:
        return game(i,num1,start,m-1)
    else:
        return game(i,num1,m+1,end)
for i in num2:
    start=0
    end=len(num1)-1
    print(game(i,num1,start,end),end=' ')
