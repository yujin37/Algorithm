#실버4, 숫자카드 2
import sys
n=int(sys.stdin.readline())
num1=sorted([*map(int,sys.stdin.readline().split())])
m=int(input())
num2=[*map(int,sys.stdin.readline().split())]
result={}
for i in num1:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
def search(arr, target, start, end):
    if start>end:
        return 0
    m=(start+end)//2
    if arr[m]==target:
        return result.get(target)
    elif arr[m]<target:
        return search(arr, target, m+1,end)
    else:
        return search(arr, target, start, m-1)
for target in num2:
    print(search(num1,target,0,len(num1)-1),end=' ')
