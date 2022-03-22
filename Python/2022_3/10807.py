#개수 세기
n=int(input())
num=list(map(int,input().split()))
count=0
v=int(input())
for i in range(n):
    if(num[i]==v):
        count+=1
print(count)
