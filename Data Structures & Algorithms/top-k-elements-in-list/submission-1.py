import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visit = []
        count_dict = {}
        for i in nums:
            if i in visit:
                continue
            count = nums.count(i)
            count_dict[i] = count
            visit.append(i)
        highest_values = [num for num, freq in heapq.nlargest(k, count_dict.items(), key=lambda x: x[1])]
        return highest_values