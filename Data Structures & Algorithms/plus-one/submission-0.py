class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        result = result + 1
        out = []
        for i in str(result):
            out.append(i)

        return out 

        