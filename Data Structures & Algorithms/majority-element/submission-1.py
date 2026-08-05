class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_dict = {}
        for i in nums:
            if i in hash_dict:
                hash_dict[i] = hash_dict[i] +1
                if hash_dict[i] >= (len(nums)/2):
                    return i
            else:
                hash_dict[i] = 1
        return i