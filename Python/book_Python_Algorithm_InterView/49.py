import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sort = strs[:]
        for i in range(len(strs_sort)):
            strs_sort[i] = ''.join(sorted(strs_sort[i]))
        result = collections.defaultdict(list)
        for i in range(len(strs)):
            result[strs_sort[i]].append(strs[i])
        return list(result.values())