#통계학
from collections import Counter
import sys
n=int(sys.stdin.readline())
list=[]#숫자담기

for i in range(n):#숫자추가
    list.append(int(sys.stdin.readline()))
list.sort()#정렬
cnt=Counter(list).most_common()
print(round(sum(list)/n))#산술평균
print(list[n//2])#중앙값
if(len(cnt)>1):
    if cnt[0][1] == cnt[1][1]:#빈도수가 같은 것들 발생
        print(cnt[1][0])#2번째로 작은 것 출력
    else:
        print(cnt[0][0])#아니라면 첫번째것 출력하며ㅕㄴ 됨
else:
    print(cnt[0][0])#길이가 넘지 않아도 첫번째거 출력
#빈도값
print(list[-1]-list[0])#최댓값-최솟값
