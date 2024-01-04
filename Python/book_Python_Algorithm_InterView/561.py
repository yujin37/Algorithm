from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        
        nums.sort()

        check = []

        for i in range(len(nums)):

            check.append(nums[i])
            if len(check) == 2:
                sum += min(check)
                check = []
        return sum