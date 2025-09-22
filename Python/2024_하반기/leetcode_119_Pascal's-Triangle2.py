class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        triangle = []
        for i in range(rowIndex+1):
            if i == 0: #첫번째
                triangle.append([1])
            elif i == 1: #두번째
                triangle.append([1,1])
            else:
                sub = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        sub.append(1)
                    else:
                        num = triangle[i-1][j-1] + triangle[i-1][j]
                        sub.append(num)
                        #print("상태", sub)
                triangle.append(sub)
                
        #print(triangle)
        return triangle[-1]