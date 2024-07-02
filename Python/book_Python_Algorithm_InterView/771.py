class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_check = dict()
        for jewel in jewels:
            jewels_check[jewel] = 0
        for stone in stones:
            if stone in jewels_check:
                jewels_check[stone] += 1
        result = 0
        for _, value in jewels_check.items():
            result += value
        return result
        