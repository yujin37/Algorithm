import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort() #정렬을 하고
    heapq.heapify(scoville) #힙 형태로 바꾼 뒤
    if scoville[0] > K: #가장 작은 값이 k보다 크면 나머지 크다는 의미 
        return answer #바로 리턴
    
    while scoville[0]< K:
        
        if len(scoville) == 1: #끝까지 와도 안되면
            return -1 #불가 표시 리턴
        #나머지 경우에는 계속 섞어본다.  
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        score = first + second * 2
        heapq.heappush(scoville, score) #스코빌 지수 넣어준다.
        answer += 1 #횟수를 올려줌
    return answer
        

scoville = [1,2,3,9,10,12]
K = 7
print(solution(scoville, K))
print('--------')
scoville = [1,1,2,2,6]
K = 4
print(solution(scoville,K))