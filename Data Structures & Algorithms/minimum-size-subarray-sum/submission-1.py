class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        left =0
        sum_cur = 0
        for right in range(0,len(nums)):
            sum_cur = sum_cur + nums[right]
            while sum_cur >= target :
                
                min_length = min(right-left+1,min_length)
                sum_cur = sum_cur - nums[left]
                left = left+1
                
            right = right +1 
        return 0 if min_length == float("inf") else min_length

