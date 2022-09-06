def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        cutting=[]
        for j in range(commands[i][0]-1,commands[i][1]):
            cutting.append(array[j])
        cutting.sort()
        answer.append(cutting[commands[i][2]-1])
        #print(answer)
    return answer
