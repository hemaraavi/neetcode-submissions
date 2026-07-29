class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_s_hashmap = {}
        string_t_hashmap = {}
        for each_str in s:
            if each_str in string_s_hashmap:
                string_s_hashmap[each_str] =string_s_hashmap[each_str]+1
            else:
                string_s_hashmap[each_str] = 1
        for each_str in t:
            if each_str in string_t_hashmap:
                string_t_hashmap[each_str] =string_t_hashmap[each_str]+1
            else:
                string_t_hashmap[each_str] = 1
        if string_s_hashmap == string_t_hashmap:
            return True
        return False