#bronze3
N=int(input())

arr=list(map(int, input().split())) #리스트 형태로 숫자를 입력받음
max=arr[0]//최댓값을 일단 첫번째것으로 설정
min=arr[0]//최솟값을 일단 첫번째것으로 설정
for i in arr[1:]:#처음부터 끝까지 봐주면 되므로 이렇게
    if(max<i):
        max=i
    if(min>i):
        min=i
print(min, max)#비교해서 최종적으로 최대최소 출력
