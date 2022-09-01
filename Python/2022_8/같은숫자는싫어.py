def solution(arr):
    answer = []
    for i in arr:
        if i==answer[-1]:
            pass
        else:
            answer.append(i)
    return answer
