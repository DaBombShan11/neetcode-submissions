class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        med = (low + high) // 2 
        while low <= high:
            if nums[med] == target:
                return med
            elif nums[med] > target:
                high = med - 1 
            else:
                low = med + 1 
            med = (low + high) // 2

        return -1 

        