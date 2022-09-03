def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
    max0=0
    max1=0
    for i in range(len(sizes)):
        if max0<sizes[i][0]:
            max0=sizes[i][0]
        if max1<sizes[i][1]:
            max1=sizes[i][1]
    #sizes.sort(key=lambda x:(x[0],x[1]))
    #print(max0,max1)
    answer=max0*max1
    return answer
