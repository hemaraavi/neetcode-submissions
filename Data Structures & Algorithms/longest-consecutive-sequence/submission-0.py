class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = 0
        set_nums = set(nums)
        for i in set_nums:
            if (i-1) in set_nums:
                continue
            next_elem = i+1
            seq = 1
            while  next_elem in set_nums:
                seq = seq+1
                next_elem = next_elem+1
            max_sequence = max(max_sequence,seq)
        return max_sequence