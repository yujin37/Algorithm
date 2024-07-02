import heapq
n = int(input())

heap = []
init_number = list(map(int,input().split()))


for num in init_number:
    heapq.heappush(heap, num)

for i in range(n-1):
    numbers = list(map(int,input().split())) #처음에 리스터 형태로 받고

    for num in numbers: #이제 각 숫자들을 
        if heap[0] < num: #기존에 들어있는 숫자와 비교해서 큰 숫자가 있으면
            heapq.heappush(heap,num) #넣어주고
            heapq.heappop(heap) #기존에 작은 값은 뽑아준다.
print(heap[0]) #n만큼의 길이로 0번째가 n번째 큰수이다. 
