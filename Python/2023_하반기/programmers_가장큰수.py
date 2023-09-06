def solution(numbers):
    
    #문자열로 변환
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key = lambda x:x*3, reverse = True)
    answer = str(int(''.join(numbers))) 
            
    return answer
print(solution([6,10,2]))
print('-----')
print(solution([3, 30, 34, 5, 9]))