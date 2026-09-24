class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        final_count = 0
        for i in num_set:
            if i-1 not in num_set:
                iterator = 1
                value = 1
                while i + iterator in num_set:
                    iterator = iterator + 1
                    value = value + 1
                if final_count < value:
                    final_count = value

        return final_count
        