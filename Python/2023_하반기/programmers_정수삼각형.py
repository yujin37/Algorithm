def solution(triangle):
    answer = 0
    #top_down방식
    triangle_len = len(triangle)
    for i in range(1,triangle_len):
        for j in range(len(triangle[i])): 
            if j == len(triangle[i])-1: #오른쪽 끝
                triangle[i][j] += triangle[i-1][j-1]
            elif j==0: #왼쪽 끝
                triangle[i][j] +=  triangle[i-1][j]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    answer = max(triangle[triangle_len-1])
    
    return answer
def solution2(triangle):
    answer = 0
    #bottom-up 방식
    for i in range(len(triangle)-1,-1,-1):
        for j in range(0,i):
            triangle[i-1][j]+=max(triangle[i][j], triangle[i][j+1])
    answer = triangle[0][0]
    return answer
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	
print(solution(triangle))
print('---------')
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	
print(solution2(triangle))