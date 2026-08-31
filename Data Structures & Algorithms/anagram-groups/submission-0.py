class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newList = []
        all_anagrams = []
        for i in strs:
            newList.append(sorted(i))
        for i in newList:
            anagrams = []
            for idx, j in enumerate(newList):
                if i == j:
                    if any(strs[idx] in sublist for sublist in all_anagrams):
                        continue
                    anagrams.append(strs[idx])
            if len(anagrams) != 0:
                all_anagrams.append(anagrams)
        return all_anagrams