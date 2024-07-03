class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_count = [0] * (n+1)
        trust_by_count = [0] * (n+1)

        for me, you in trust:
            trust_count[me] += 1
            trust_by_count[you] += 1
        
        for i in range(1, n+1):
            if trust_count[i] == 0 and trust_by_count[i] == n-1:
                return i
        return -1

solution = Solution()
n = 3
trust = [[1,3],[2,3],[3,1]]
print(solution.findJudge(n, trust))