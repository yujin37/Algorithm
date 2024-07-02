def solution(numbers, hand):
    answer = ''
    
    # key 패드 제작
    key = dict()
    num = 1
    
    for i in range(4):
        for j in range(3):
            if num == 10:
                key['*'] = [i,j]
            elif num == 11:
                key[0] = [i,j]
            elif num == 12:
                key['#'] = [i,j]
            else:
                key[num] = [i,j]
            num+=1
    left = key['*']
    right = key['#']
    for i in numbers:
        
        if i in [1,4,7]:
            left = key[i]
            answer += 'L'
        elif i in [3,6,9]:
            right = key[i]
            answer += 'R'
        else:
            check_left = abs(key[i][0] - left[0]) + abs(key[i][1] - left[1])
            check_right = abs(key[i][0] - right[0]) + abs(key[i][1] - right[1])
            if check_left < check_right:
                left = key[i]
                answer += 'L'
            elif check_left > check_right:
                right = key[i]
                answer += 'R'
            else:
                if hand == 'left':
                    left = key[i]
                    answer += 'L'
                else:
                    right = key[i]
                    answer += 'R'
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"

print(solution(numbers, hand))