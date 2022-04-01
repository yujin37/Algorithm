#이 문제도 이중 for문 불가. if문으로 풀어주어야 함.
#elif에서 j를 빼주는 이유는 크면 결국은 성립 안된다는 의미이기 때문이다.
n=int(input())
num=list(map(int,input().split()))
x=int(input())
count=0

num.sort()

i=0
j=len(num)-1
while i!=j:
    if(num[i]+num[j]==x):
        count+=1
        i+=1
    elif(num[i]+num[j]>x):
        j-=1
    else:i+=1
print(count)
