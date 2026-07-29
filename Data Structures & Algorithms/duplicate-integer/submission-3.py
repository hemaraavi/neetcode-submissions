class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_array = set()
        for i in nums:
            if i not in new_array:
                new_array.add(i)
            else:
                return True
        return False