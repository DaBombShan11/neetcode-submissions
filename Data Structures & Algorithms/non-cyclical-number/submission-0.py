class Solution:
    def isHappy(self, n: int) -> bool:
        # to keep track of sums already seen
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            total = 0 
            for i in str(n):
                total = total + int(i) * int(i)
            n = total 
        return True 