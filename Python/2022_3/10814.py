#나이순정렬
import sys#입력시간 감소 위한 작업
n=int(sys.stdin.readline())
agename=[]

for _ in range(n):
    agename.append(list(sys.stdin.readline().split()))#한번에 리스트 형태로 받음

agename.sort(key=lambda x:int(x[0]))#나이를 기준으로 정렬
#파이썬에서는 별도로 입력 순을 지정안해줘도 되는데 stable형태이기 때문에 알아서 배열이 정해진다.

for i in agename:
    print(i[0],i[1])#2차원 배열이므로 for문 접근후 0,1로 출력이 가능하다.
