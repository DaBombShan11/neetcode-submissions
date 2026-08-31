class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        index = 0
        product = 1
        for i in nums:
            for idx, j in enumerate(nums):
                if idx == index:
                    continue
                product = product * j
            products.append(product)
            product = 1
            index = index + 1
        return products