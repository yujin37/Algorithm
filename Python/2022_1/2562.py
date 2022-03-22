#bronze2
arr=[]#리스트를 설정하고
for i in range(9):#9까지 입력받는다.
    arr.append(int(input()))#append형태로 입력을 받는다.
print(max(arr))#파이썬은 max()를 통해 알아서 최댓값 찾아준다.
print(arr.index(max(arr))+1)#자리도 .index라는 것을 통해 찾아준다. 
