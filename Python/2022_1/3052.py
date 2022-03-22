#bronze2
arr=[]
for i in range(10):
    N=int(input())
    arr.append(N%42) #리스트에 추가해줄 때에는 append해주어서 넣어주고 ()에는 사칙연산도 가능
arr=set(arr)#중복을 제거할 수 있는 파이썬의 문법

print(len(arr))
