class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Products of everything to the LEFT
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Products of everything to the RIGHT
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result