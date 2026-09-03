class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sorted_text = "".join(sorted(word))

            if sorted_text not in groups:
                groups[sorted_text] = [word]
            else:
                groups[sorted_text].append(word)

        final_list = [v for v in groups.values()]
        return final_list