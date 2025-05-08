class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))

        return n == 1