class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def calculate_height(r, b, start_red):
            height = 0
            now = 1
            while r>= 0 and b >= 0:
                #홀수층이고 빨간색 시작이면 . 짝수층인데 파란색 시작이었으면 red 삭제
                if (now % 2 == 1 and start_red) or (now % 2 == 0 and not start_red):
                    r -= now
                else: #그외의 경우에는 blue를 삭제
                    b -= now
                if r >= 0 and b >= 0: #층을 생성되는지 체크해서 추가
                    height += 1
                now += 1 #현재 위치를 업데이트
            return height
        
        height_red = calculate_height(red, blue, True) #red 먼저일때
        height_blue = calculate_height(red, blue, False) #blue 먼저일때
        return max(height_red, height_blue)
        

solution = Solution()
print(solution.maxHeightOfTriangle(2, 4))