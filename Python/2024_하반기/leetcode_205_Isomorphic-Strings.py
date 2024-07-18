class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_check, t_check = dict(), dict()
        s_result, t_result = '', ''
        n1, n2 = 1, 1
        for s_sub in s:
            # s check
            if s_sub in s_check:
                s_result += str(s_check[s_sub])
            else:
                s_check[s_sub] = n1
                s_result += str(n1)
                n1 += 1
        for t_sub in t:
            # t check
            if t_sub in t_check:
                t_result += str(t_check[t_sub])
            else:
                t_check[t_sub] = n2
                t_result += str(n2)
                n2 += 1
        if s_result == t_result:
            return True
        else:
            return False
        