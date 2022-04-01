#좌표압축
import sys
n=int(sys.stdin.readline())
result=[]
num=list(map(int,sys.stdin.readline().split()))#리스트 형태로 받는다
num_1=sorted(list(set(num)))#겹치는 값은 없게 정렬
result={num_1[i]:i for i in range(len(num_1))}#num_1값에 자리를 표시해주는 딕셔너리

for i in num:#num는 입력받은 그대로이므로 그 값이 있을때
    print(result[i],end=' ')#key를 검색하면 value 값이 나온다. []에 key값 넣기
