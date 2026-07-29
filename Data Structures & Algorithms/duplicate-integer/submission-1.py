class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compare_set = set() 
        for i in nums: 
            if i not in compare_set: 
                compare_set.add(i) 
            else: return True 
        return False