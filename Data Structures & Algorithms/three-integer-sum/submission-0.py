class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplet_list = []

        for i in range(len(nums)):
            # Skip duplicate starting values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = len(nums) - 1

            while low < high:
                pair_sum = nums[low] + nums[high]

                if pair_sum == -nums[i]:
                    triplet = [nums[i], nums[low], nums[high]]
                    triplet_list.append(triplet)

                    low = low + 1
                    high = high - 1

                    # Skip duplicate low values
                    while low < high and nums[low] == nums[low - 1]:
                        low = low + 1

                    # Skip duplicate high values
                    while low < high and nums[high] == nums[high + 1]:
                        high = high - 1

                elif pair_sum > -nums[i]:
                    high = high - 1

                else:
                    low = low + 1

        return triplet_list