#실버3 2559 수열
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
temp=list(map(int,input().split())) #일단 리스트로 만들고

total=[]
total.append(sum(temp[:K])) #일단 첫번째 수를 계산해준다.

for i in range(N-K):
    total.append(total[i]-temp[i]+temp[i+K]) #그리고 매번 범위에서 바로 앞에것을 버려주고 그 뒤에 것을 해주면 된다. 몇개이든 상관없음.
print(max(total))
