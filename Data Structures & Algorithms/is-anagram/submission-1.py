class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        s_dict = {}
        t_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] = s_dict[i] + 1
        for j in t:
            if j not in t_dict:
                t_dict[j] = 1
            else:
                t_dict[j] = t_dict[j] + 1

        # sorted_s_dict = dict(sorted(s_dict.items()))
        # sorted_t_dict = dict(sorted(t_dict.items()))
        return (s_dict == t_dict)