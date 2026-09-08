class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len_str = min(len(word1),len(word2))
        result_str = ""
        for i in range(0,min_len_str):
            result_str = result_str + word1[i]+word2[i]

        result_str = result_str+word1[i+1:]+word2[i+1:]
        return result_str
