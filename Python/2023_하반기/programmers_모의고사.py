def solution(answers):
    answer = [1]
    math_1 = [1,2,3,4,5]
    math_2 = [2,1,2,3,2,4,2,5]
    math_3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer_1 = 0
    answer_2 = 0
    answer_3 = 0 
    for i in range(len(answers)):
        if math_1[i % len(math_1)] == answers[i]:
            answer_1 += 1
        if math_2[i % len(math_2)] == answers[i]:
            answer_2 += 1
        if math_3[i % len(math_3)] == answers[i]:
            answer_3 += 1
    result = [answer_1, answer_2, answer_3]
    
    num = answer_1

    for i in range(1,3):
        if num < result[i]:
            num = result[i]
            answer = [i+1]
        elif num == result[i]:
            answer.append(i+1)
        else:
            pass
    
    return answer