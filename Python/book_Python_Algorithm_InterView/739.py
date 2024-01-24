from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) #전체 온도 길이
        stack = []
        result = [ 0 for _ in range(n)]

        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()

                result[last] = i - last
            stack.append(i)

        return result

