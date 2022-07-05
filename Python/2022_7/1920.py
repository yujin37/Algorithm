#실버4 수 찾기
import sys
n1=sys.stdin.readline()
num1=sorted(map(int,sys.stdin.readline().split()))
n2=sys.stdin.readline()
num2=map(int,sys.stdin.readline().split())

def binary(i,num1,start,end):
    if start>end:
        return 0
    m=(start+end)//2
    if i == num1[m]:
        return 1
    elif i<num1[m]:
        return binary(i,num1,start,m-1)
    else:
        return binary(i,num1,m+1,end)
for i in num2:
    start=0
    end=len(num1)-1
    print(binary(i,num1, start,end))
