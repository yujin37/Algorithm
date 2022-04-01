#홀수
list=[]
for i in range(7):
    n=int(input())
    if(n%2!=0):
        list.append(n)
if(len(list)!=0): 
    print(sum(list)) 
    print(min(list))
else:
    print("-1")
