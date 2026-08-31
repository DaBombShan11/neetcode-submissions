class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_a, i in enumerate(nums):
            for idx_b, j in enumerate(nums):
                if i + j == target and idx_a != idx_b:
                    return [idx_a, idx_b]
        return False