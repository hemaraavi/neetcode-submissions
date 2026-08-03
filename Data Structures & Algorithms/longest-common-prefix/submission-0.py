class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for len_str,i in enumerate(strs[0]):
            for each_str in strs[1:]:
                if (len_str==len(each_str) or each_str[len_str]!=i):
                    return each_str[:len_str]
        return strs[0]