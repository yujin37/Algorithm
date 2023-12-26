from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        place = len(s)-1
        
        for i in range(0,len(s)//2):
            s[i], s[place-i] = s[place-i], s[i]
        
        