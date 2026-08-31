class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = []
        val = False
        for i in nums:
            if i in duplicate:
                return True
            duplicate.append(i)
        return val
        