#다시 풀어야 할 문제
#실버2 조합 0의 개수, 팩토리얼로 안풀리는 문제
#10을 만들기 위해 2와 5의 개수 중 작은 것을 계산.
def count_two(n):#2로 나누는 것 카운트 하는 함수
    cnt=0
    while n>0:
        n=n//2
        cnt+=n#몫을 더해준다.
    return cnt#카운트 값 반환

def count_five(n):#5로 나누는 것 카운트 하는 함수
    cnt=0
    while n>0:
        n=n//5
        cnt+=n#몫을 더해주는 것이다.
    return cnt##카운트 값 반환

def count_zero(num1, num2):#각 경우에 대해 카운트
    t=count_two(num1)-count_two(num2)-count_two(num1-num2)#겹치는 카운트 역시 빼주어야 함
    f=count_five(num1)-count_five(num2)-count_five(num1-num2)
    return min(t,f)

x,y=map(int,input().split())
print(count_zero(x,y))
